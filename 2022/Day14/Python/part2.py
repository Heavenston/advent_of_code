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

def place_sand(board):
    x = 500
    y = 0
    while y < 998:
        if board[x][y+1] == ".":
            y += 1
        elif board[x-1][y+1] == ".":
            y += 1
            x -= 1
        elif board[x+1][y+1] == ".":
            y += 1
            x += 1
        else:
            break
    board[x][y] = "O"
    return board[x][y+1] == "#" or board[x][y+1] == "O"

def day14(contents: str):
    lines = contents.split("\n")
    
    board = [["." for _ in range(1000)] for _ in range(1000)]

    max_y = 0
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue
            
        rocks = l.split(" -> ")
        for j in range(len(rocks)-1):
            [x1, y1] = rocks[j].split(",")
            [x2, y2] = rocks[j+1].split(",")
            x1 = int(x1); x2 = int(x2)
            y1 = int(y1); y2 = int(y2)
            max_y = max(max_y, y1, y2)
            if x1 == x2:
                start = min(y1, y2)
                end = max(y1, y2)
                for y in range(start, end+1):
                    board[x1][y] = "#"
            else:
                start = min(x1, x2)
                end = max(x1, x2)
                for x in range(start, end+1):
                    board[x][y1] = "#"

    printBoard([a[:10] for a in board[494:504]])

    for x in range(len(board[0])):
        board[x][max_y+2] = "#"

    printBoard([a[:10] for a in board[494:504]])

    i = 0
    while board[500][0] != "O":
        place_sand(board)
        i += 1
    return i

inputFile = open("../input.txt","r")
print(day14(inputFile.read()))


