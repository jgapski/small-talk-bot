-module(python_improver).

-export([improve/1]).

-spec improve(map()) -> [binary()].
improve(#{<<"msg">> := Msg}) ->
        emotional_meaning(Msg).

emotional_meaning(Msg) ->
        Cmd = "python config/python/messages_analysic.py '" ++ binary_to_list(Msg) ++ "'",
        R = os:cmd(Cmd),
        [list_to_binary(R)].

