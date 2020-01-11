-module(db).

-record(msg, {from, content, ref}).

-behaviour(gen_server).

-define(ASAP_TIMEOUT, timer:seconds(5)).

%% API
-export([add_msg/2, start_link/0]).

-export([code_change/3, handle_call/3, handle_cast/2,
	 handle_info/2, init/1, terminate/2]).

start_link() ->
    gen_server:start_link({local, ?MODULE}, ?MODULE, [],
			  []).

add_msg(From, Msg) ->
    case consists_ASAP(Msg) of
        "0\n" -> [];
        _ ->
            Ref = erlang:make_ref(),
            NewMsg = #msg{from = From, content = Msg, ref = Ref},
            gen_server:call(?MODULE, {add, NewMsg})
    end.

consists_ASAP(Msg) ->
    Cmd = "python src/python/ASAP_detector.py " ++ binary_to_list(Msg),
    R = os:cmd(Cmd),
    logger:error("~p", [R]),
    R.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

init(_Args) -> {ok, []}.

handle_call({add, Msg = #msg{ref = Ref}}, _From, State) ->
    logger:error("Msg ~p added, State is ~p", [Msg, State]),
    erlang:send_after(?ASAP_TIMEOUT, self(), {del, Ref}),
    {reply, [], [Msg | State]}.

handle_info({del, Ref}, State) ->
    NewState = lists:filter(fun (#msg{ref = R})
				    when R == Ref ->
				    false;
				(_) -> true
			    end,
			    State),
    logger:error("MsgRef ~p deleted, OldState = ~p, NewState "
		"= ~p",
		[Ref, State, NewState]),
    {noreply, NewState}.

handle_cast(_Msg, State) -> {noreply, State}.

terminate(_Reason, _State) -> ok.

code_change(_OldVsn, State, _Extra) -> {ok, State}.
