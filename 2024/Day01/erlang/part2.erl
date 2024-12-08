-module(part2).
-export([main/0]).

countTimes(Elem, [El | Rest]) ->
    if Elem == El -> 1;
       true -> 0 end + countTimes(Elem, Rest);
countTimes(_, []) -> 0
.

main() ->
    { ok, Input } = file:read_file("../input.txt"),

    Lines = lists:filter(
        fun(Line) -> not string:is_empty(Line) end,
        string:split(Input, "\n", all)
    ),
    List1 = lists:map(
        fun(A) -> list_to_tuple(
            lists:map(
                fun(B) -> element(1, string:to_integer(B)) end,
                string:split(A, "   ", all)
            )
        ) end,
        Lines
    ),
    {L1, L2} = lists:unzip(List1),

    Sum = lists:sum(lists:map(fun(Val) -> Val * countTimes(Val, L2) end, L1)),

    io:format("~kp~n", [Sum])
    %% io:format("~kp~n", [List1])
   
.
