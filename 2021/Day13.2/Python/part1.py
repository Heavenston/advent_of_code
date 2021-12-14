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

def foldY(board: list[list[str]], pos: int) -> list[list[str]]:
    return createBoard(
        boardWidth(board),
        pos,
        lambda x, y: "#" if board[x][y] == "#" or board[x][pos+abs(pos-y)] == "#" else "."
    )
def foldX(board: list[list[str]], pos: int) -> list[list[str]]:
    return createBoard(
        pos,
        boardHeight(board),
        lambda x, y: "#" if board[x][y] == "#" or board[pos+abs(pos-x)][y] == "#" else "."
    )

def day13(contents: str):
    parts = contents.split("\n\n")
    positions = list(map(lambda g: list(map(parseNum, g.split(","))), parts[0].split("\n")))
    folds = parts[1].split("\n")[:-1]

    width = 0
    height = 0
    for [x, y] in positions:
        if x >= width:
            width = x+1
        if y >= height:
            height = y+1
    board = createBoard(width, height, lambda x, y: ".")
    for [x, y] in positions:
        board[x][y] = "#"

    for fold in folds[0:1]:
        s = fold.split("=")
        axis = s[0][-1]
        pos = int(s[1])

        if axis == "x":
            board = foldX(board, pos)
        elif axis == "y":
            board = foldY(board, pos)
        else:
            raise Exception("djqlkdjsqljd")

    s = 0
    for (x, y) in posIter(board):
        if board[x][y] == "#":
            s += 1

    return s

inputFile = open("../input.txt","r")
print(day13(inputFile.read()))


