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

def day15(contents: str):
    lines = contents.split("\n")
    
    cannot_contain = set()
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue

        [part1, part2] = l.split(":")

        [x1, y1] = part1.split(", ")
        x1 = int(x1[10:].split("=")[1])
        y1 = int(y1.split("=")[1])

        [x2, y2] = part2.split(", ")
        x2 = int(x2[22:].split("=")[1])
        y2 = int(y2.split("=")[1])

        dist = abs(y1 - y2) + abs(x2 - x1)
        dist2y = abs(y1 - 2000000)
        dist -= dist2y
        if dist > 0:
            cannot_contain = cannot_contain | set(x1 + dx for dx in range(-dist, dist+1))
    
    return len(cannot_contain)-1

inputFile = open("../input.txt","r")
print(day15(inputFile.read()))


