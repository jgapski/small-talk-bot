-module(erlang_improver).

-export([improve/1]).

improve(#{<<"from">> := From, <<"msg">> := Msg}) ->
    [] ++
    save_and_detect_ASAPs(From, Msg).

save_and_detect_ASAPs(From, Msg) ->
    db:add_msg(From, Msg).
