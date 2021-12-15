from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

"""
Matrixes or Board utils
"""
def boardWidth(board: list[list[Any]]) -> int:
    return len(board)
def boardHeight(board: list[list[Any]]) -> int:
    return len(board[0])

def parseBoard(text: str):
    return list(map(lambda g: list(g), text.split("\n")[:-1]))
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

neighborList = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def neighbors(width: int, height: int, x: int, y: int):
    return (
        (x+dx, y+dy)
        for (dx, dy) in neighborList
        if x+dx >= 0 and x+dx < width and y+dy >= 0 and y+dy < height
    )


def day15(contents: str):
    board = [[parseNum(x) for x in l] for l in parseBoard(contents)]
    (width, height) = (boardWidth(board), boardHeight(board))
    costBoard = createBoard(width, height, lambda x, y: 9999999999999)
    costBoard[0][0] = 0

    end = False
    while not end:
        end = True
        for (x, y) in posIter(board):
            for (nx, ny) in neighbors(width, height, x, y):
                if board[x][y]+costBoard[nx][ny] < costBoard[x][y]:
                    costBoard[x][y] = board[x][y]+costBoard[nx][ny]
                    end = False

    return costBoard[-1][-1]

inputFile = open("../input.txt","r")
print(day15(inputFile.read()))


