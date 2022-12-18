from collections.abc import Callable, Iterator
from collections import deque
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

def is_act(acts, x, y, z):
    if x < 0 or y < 0 or z < 0:
        return False
    if x >= 30 or y >= 30 or z >= 30:
        return False
    return acts[x][y][z]

def day18(contents: str):
    lines = contents.split("\n")
    
    activated = [[[False for _ in range(30)] for _ in range(30)] for _ in range(30)]
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue
        [x, y, z] = l.split(",")
        x = int(x)
        y = int(y)
        z = int(z)

        activated[x][y][z] = True

    surface = 0
    for x in range(30):
        for y in range(30):
            for z in range(30):
                if not is_act(activated, x, y, z):
                    continue
                if not is_act(activated, x+1, y, z):
                    surface += 1
                if not is_act(activated, x-1, y, z):
                    surface += 1
                if not is_act(activated, x, y+1, z):
                    surface += 1
                if not is_act(activated, x, y-1, z):
                    surface += 1
                if not is_act(activated, x, y, z+1):
                    surface += 1
                if not is_act(activated, x, y, z-1):
                    surface += 1
    return surface

inputFile = open("../input.txt","r")
print(day18(inputFile.read()))


