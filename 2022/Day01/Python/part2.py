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
    
# FQLKDJQLKSDJQKLSDJ

def day01(contents: str):
    lines = contents.split("\n")
    elfes = [0 for _ in range(20000)]
    
    i = 0
    for l in lines:
        print(l, i)
        if l.strip() == "":
            i += 1
            continue
        elfes[i] += int(l)

    t = 0
    a = max(enumerate(elfes), key = lambda x: x[1])[0]
    t += elfes[a]
    elfes.pop(a)
    a = max(enumerate(elfes), key = lambda x: x[1])[0]
    t += elfes[a]
    elfes.pop(a)
    a = max(enumerate(elfes), key = lambda x: x[1])[0]
    t += elfes[a]
    elfes.pop(a)
    print(t)

    pass

# FQLKDJQLKSDJQKLSDJ

inputFile = open("../input.txt","r")
print(day01(inputFile.read()))


