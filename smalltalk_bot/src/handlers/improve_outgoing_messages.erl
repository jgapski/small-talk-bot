-module(improve_outgoing_messages).

-export([init/2]).

init(Req0, Opts) ->

    {ok, Data, Req1} = cowboy_req:read_body(Req0),
    DecodedMsg = jiffy:decode(Data, [return_maps]),

    Suggestions =
        erlang_improver:improve(DecodedMsg)
        ++ python_improver:improve(DecodedMsg),

    Response = jiffy:encode(#{ suggestions => Suggestions}),
	Req2 = cowboy_req:reply(200, #{
		<<"content-type">> => <<"text/plain">>
	}, Response, Req1),
    {ok, Req2, Opts}.

