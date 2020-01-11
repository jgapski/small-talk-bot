-module(smalltalk_bot_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    smalltalk_bot_sup:start_link().

stop(_State) ->
    ok.
