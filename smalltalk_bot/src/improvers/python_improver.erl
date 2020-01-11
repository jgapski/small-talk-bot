-module(python_improver).

-export([improve/1]).

-spec improve(map()) -> [binary()].
improve(#{<<"msg">> := Msg}) ->
        check_it(Msg).

check_it(Msg) ->
        Pat = "python src/python/messages_analysic.py " ++ binary_to_list(Msg),
        R = os:cmd(Pat),
        logger:error("~p", [R]),
        R.

