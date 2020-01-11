-module(improve_outgoing_messages).

-export([init/2]).

init(Req0, Opts) ->

    {ok, Data, Req1} = cowboy_req:read_body(Req0),
    DecodedMsg = jsone:decode(Data),

    Suggestions =
        erlang_improver:improve(DecodedMsg)
        ++ python_improver:improve(DecodedMsg),

    Response = jsone:encode(#{ suggestions => Suggestions}),
	Req2 = cowboy_req:reply(200, #{
		<<"content-type">> => <<"text/plain">>
	}, Response, Req1),
    {ok, Req2, Opts}.

