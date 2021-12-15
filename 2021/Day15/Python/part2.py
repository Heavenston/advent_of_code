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
def posIter(board: list[list[Any]]):
    return (
        (x, y)
        for x in range(boardWidth(board))
        for y in range(boardHeight(board))
    )
def posIter2(width: int, height: int):
    return (
        (x, y)
        for x in range(width)
        for y in range(height)
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
    costBoard = createBoard(width * 5, height * 5, lambda x, y: 9999999999999)
    costBoard[0][0] = 0

    def getBoard(x: int, y: int):
        return (board[x%width][y%height] + (x//width) + (y//height) - 1) % 9 + 1

    end = 500
    while end != 0:
        end = 0
        for (x, y) in posIter2(width * 5, height * 5):
            for (nx, ny) in neighbors(width * 5, height * 5, x, y):
                if getBoard(x,y)+costBoard[nx][ny] < costBoard[x][y]:
                    costBoard[x][y] = getBoard(x,y)+costBoard[nx][ny]
                    end += 1
        print(end)

    return costBoard[-1][-1]

inputFile = open("../input.txt","r")
print(day15(inputFile.read()))


