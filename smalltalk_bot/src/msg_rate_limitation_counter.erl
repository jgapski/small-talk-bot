-module(msg_rate_limitation_counter).

-record(msg, {from, content, ref}).

-behaviour(gen_server).

-define(TIMEOUT, timer:seconds(5)).
-define(MSGS_COUNT, 3).

%% API
-export([add_msg/2, start_link/0]).

-export([code_change/3, handle_call/3, handle_cast/2,
	 handle_info/2, init/1, terminate/2]).

start_link() ->
    gen_server:start_link({local, ?MODULE}, ?MODULE, [],
			  []).

add_msg(From, Msg) ->
            Ref = erlang:make_ref(),
            NewMsg = #msg{from = From, content = Msg, ref = Ref},
            gen_server:call(?MODULE, {add, NewMsg}).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

init(_Args) -> {ok, []}.

handle_call({add, Msg = #msg{ref = Ref, from = From}}, _, State) ->
    Reply = make_reply(From, State),
    erlang:send_after(?TIMEOUT, self(), {del, Ref}),
    {reply, Reply, [Msg | State]}.

make_reply(From, State) ->
    Msgs = lists:filter(fun(#msg{from = F}) -> F == From end, State),
    case length(Msgs) > ?MSGS_COUNT of
        true -> [<<"Take it easy, do not spam so many messages in such short time">>];
        _ -> []
    end.

handle_info({del, Ref}, State) ->
    NewState = lists:filter(fun (#msg{ref = R}) -> R =/= Ref
			    end, State),
    {noreply, NewState}.

handle_cast(_Msg, State) -> {noreply, State}.

terminate(_Reason, _State) -> ok.

code_change(_OldVsn, State, _Extra) -> {ok, State}.
