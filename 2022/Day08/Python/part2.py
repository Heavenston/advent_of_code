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

def count(lines, x, y):
    v = int(lines[y][x])

    dxn = 0
    while (x+dxn) > 0:
        dxn -= 1
        if int(lines[y][x+dxn]) >= v:
            break


    dxp = 0
    while (x+dxp) < len(lines[y])-1:
        dxp += 1
        if int(lines[y][x+dxp]) >= v:
            break

    dyn = 0
    while (y+dyn) > 0:
        dyn -= 1
        if int(lines[y+dyn][x]) >= v:
            break

    dyp = 0
    while (y+dyp) < len(lines)-1:
        dyp += 1
        if int(lines[y+dyp][x]) >= v:
            break

    return abs(dxn) * abs(dxp) * abs(dyn) * dyp

def day08(contents: str):
    lines = contents.split("\n")[:-1]
    
    result1 = []

    for x in range(len(lines)):
        for y in range(len(lines[x])):
            result1 += [count(lines, x, y)]
    
    return max(result1)

inputFile = open("../input.txt","r")
print(day08(inputFile.read()))


