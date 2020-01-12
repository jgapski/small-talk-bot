-module(erlang_improver).

-export([improve/1]).

improve(#{<<"from">> := From, <<"msg">> := Msg}) ->
    [] ++
    save_and_detect_ASAPs(From, Msg) ++
    limit_message_rate(From, Msg).

save_and_detect_ASAPs(From, Msg) ->
    asap_rate_counter:add_msg(From, Msg).

limit_message_rate(From, Msg) ->
    msg_rate_limitation_counter:add_msg(From, Msg).
