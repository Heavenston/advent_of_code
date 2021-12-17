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


def day17(contents: str):
    [[targetXMin, targetXMax], [targetYMin, targetYMax]] = (
        contents[13:].split(", ")
        | p.map(lambda l: l[2:].split("..") | p.map(parseNum))
    )

    def test(ix: int, iy: int) -> int:
        px = 0
        py = 0

        maxHeight = 0

        while True:
            maxHeight = py if py > maxHeight else maxHeight
            if px >= targetXMin and px <= targetXMax and py >= targetYMin and py <= targetYMax:
                return maxHeight
            if py < targetYMin or px > targetXMax:
                break
            px += ix
            py += iy
            if ix != 0:
                ix -= 1 if ix > 0 else -1
            iy -= 1

        return -1

    return len(list(
        filter(
            lambda p: p != -1,
            (
                test(ix, iy)
                for ix in range(0, 500)
                for iy in range(-500, 500)
            )
        )
    ))

inputFile = open("../input.txt","r")
print(day17(inputFile.read()))


