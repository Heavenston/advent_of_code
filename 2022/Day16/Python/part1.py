from collections.abc import Callable, Iterator
from collections import deque
from dataclasses import dataclass, field
import heapq
from typing import Any, TypeVar
import pipe as p
import math

T = TypeVar("T")
U = TypeVar("U")

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

"""
Matrixes or Board utils
"""
def boardWidth(board: list[list[Any]]) -> int:
    return len(board)
def boardHeight(board: list[list[Any]]) -> int:
    return len(board[0])

def parseBoard(text: str) -> list[list[str]]:
    return transpose(list(map(lambda g: list(g), text.split("\n")[:-1])))
def transpose(board: list[list[T]]) -> list[list[T]]:
    return [[board[y][x] for y in range(len(board[0]))] for x in range(len(board))]
def createBoard(width: int, height: int, init: Callable[[int, int], T] = (lambda x, y: 0)) -> list[list[T]]:
    return [[init(x, y) for y in range(height)] for x in range(width)]
def printBoard(board: list[list[Any]]):
    for y in range(boardHeight(board)):
        line = ""
        for x in range(boardWidth(board)):
            line += str(board[x][y])
        print(line)
def posIter(board: list[list[Any]]) -> Iterator[tuple[int, int]]:
    return (
        (x, y)
        for x in range(boardWidth(board))
        for y in range(boardHeight(board))
    )
def mapBoard(mm: Callable[[int, int, T], U], board: list[list[T]]) -> list[list[U]]:
    return createBoard(boardWidth(board), boardHeight(board), lambda x, y: mm(x, y, board[x][y]))
def linearBoard(board: list[list[T]]) -> Iterator[tuple[int, int, T]]:
    return (
        (x, y, board[x][y])
        for (x, y) in posIter(board)
    )

table1 = {

}

table2 = {

}

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False) 

def day16(contents: str):
    lines = contents.split("\n")
    
    valves_conn = {}
    valves_rate = {}
    valves_stat = {}
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue
        [part1, part2] = l.split(";")
        name = part1.split(" ")[1]
        rate = int(part1.split(" ")[4].split("=")[1])
        conns = part2.split(", ")
        conns[0] = conns[0][-2:]
    
        valves_conn[name] = conns
        valves_rate[name] = rate
        valves_stat[name] = False

    q = deque([(0, "AA", 31, set())])

    f = 0

    while len(q) > 0:
        bestI, (pes, pos, mns, opened) = max(enumerate(q), key = lambda a: a[1][1] - (a[1][2] + 1))
        q.pop(bestI)

        print(mns, len(q))
        if mns <= 0:
            f = max(pes, f)
            return f
        
        pes += sum(valves_rate[n] for n in opened)

        if valves_rate[pos] != 0 and pos not in opened:
            o = set(opened)
            o.add(pos)
            p = (pos, pes + valves_rate[pos], mns - 1, o)
            if p not in q:
                q.append(p)

        for conn in valves_conn[pos]:
            p = (conn, pes, mns-1, opened)
            if p not in q:
                q.append(p)


inputFile = open("../input.txt","r")
print(day16(inputFile.read()))


