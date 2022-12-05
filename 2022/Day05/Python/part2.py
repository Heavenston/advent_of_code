from collections.abc import Callable, Iterator
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

def day05(contents: str):
    lines = contents.split("\n")
    
    column = [[] for _ in range(9)]
    
    for x in range(0, 9):
        i = 1 + x * 4
        for y in range(7, -1, -1):
            if lines[y][i] != " ":
                column[x].append(lines[y][i])
    
    for i in range(10, len(lines)-1, 1):
        l = lines[i]
        if l.strip() == "":
            continue
        
        [_m, x, _f, f, _t, t] = l.split(" ")
        x = int(x)
        f = int(f)
        t = int(t)
        
        column[t-1] += column[f-1][(-x):]
        for _ in range(x):
            column[f-1].pop()
    
    a = ""
    for c in column:
        a += c[-1]
    return a

inputFile = open("../input.txt","r")
print(day05(inputFile.read()))


