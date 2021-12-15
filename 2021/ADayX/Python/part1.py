from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

"""
Matrixes or Board utils
"""
def boardWidth(board: list[list[str]]) -> int:
    return len(board)
def boardHeight(board: list[list[str]]) -> int:
    return len(board[0])

def parseBoard(text: str):
    map(lambda g: list(g), text.split("\n"))
def createBoard(width: int, height: int, init: Callable[[int, int], T] = (lambda x, y: 0)) -> list[list[T]]:
    return [[init(x, y) for y in range(height)] for x in range(width)]
def printBoard(board: list[list[Any]]):
    for y in range(boardHeight(board)):
        line = ""
        for x in range(boardWidth(board)):
            line += str(board[x][y])
        print(line)
def posIter(board: list[list[Any]]):
    return (
        (x, y)
        for x in range(boardWidth(board))
        for y in range(boardHeight(board))
    )

def day#DAY_NUMBER#(contents: str):
    pass

inputFile = open("../input.txt","r")
print(day#DAY_NUMBER#(inputFile.read()))


