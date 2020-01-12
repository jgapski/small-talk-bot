-module(smalltalk_bot_sup).

-behaviour(supervisor).

-export([start_link/0]).

-export([init/1]).

-define(SERVER, ?MODULE).

start_link() ->
    Dispatch = cowboy_router:compile([{'_',
				       [{"/", improve_outgoing_messages,
					 []}]}]),
    {ok, _} = cowboy:start_clear(http, [{port, 8080}],
				 #{env => #{dispatch => Dispatch}}),
    supervisor:start_link({local, ?SERVER}, ?MODULE, []).

init([]) ->
    SupFlags = #{strategy => one_for_all, intensity => 0,
		 period => 1},
    ChildSpecs = [
        #{
            id => asap_rate_counter,
            start => {asap_rate_counter, start_link, []}
        },
        #{
            id => msg_rate_limitation_counter,
            start => {msg_rate_limitation_counter, start_link, []}
        }
    ],
    {ok, {SupFlags, ChildSpecs}}.
