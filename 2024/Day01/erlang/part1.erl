-module(part1).
-export([main/0]).

main() ->
    { ok, Input } = file:read_file("../input.txt"),

    Lines = lists:filter(
        fun(Line) -> not string:is_empty(Line) end,
        string:split(Input, "\n", all)
    ),
    List1 = lists:map(fun(A) -> list_to_tuple(lists:map(fun(B) -> element(1, string:to_integer(B)) end, string:split(A, "   ", all))) end, Lines),
    {L1, L2} = lists:unzip(List1),
    {SL1, SL2} = {lists:sort(L1), lists:sort(L2)},
    Couples = lists:map(fun({V1, V2}) -> abs(V1 - V2) end, lists:zip(SL1, SL2)),
    Sum = lists:sum(Couples),

    io:format("~kp~n", [Sum])
    %% io:format("~kp~n", [List1])
   
.
