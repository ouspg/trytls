#!/usr/bin/env escript
%% -*- erlang -*-
 
%% trytls (https://github.com/ouspg/trytls) stub for erlang
 
%% Uncomment the following line if needed. Hard to say if compiling is worthwhile here.
%% -mode(compile).
 
 
 
main([Url, Port]) ->
    start_deps(),
    Result = httpc:request("https://" ++ Url ++ ":" ++ Port),
    check(Result);
 
main([Url, Port, CaFile]) ->
    start_deps(),
    Result = httpc:request(head, {"https://" ++ Url ++ ":" ++ Port, []}, [{ssl,[{cacertfile, CaFile}]}], []),
    check(Result);
 
main(_) ->
    usage().
 
usage() ->
    io:format("usage: run <domain> <port> [ca_file]~n"),
    io:format("Will do request as: https://<domain>:<port>~n").
 
start_deps() ->
    inets:start(),
    ssl:start().
 
check({ok, _}) ->
    io:format("VERIFY SUCCESS~n");
 
check({error, _}) ->
    io:format("VERIFY FAILURE~n");
 
check(_) ->
    io:format("VERIFY FAILURE~n").