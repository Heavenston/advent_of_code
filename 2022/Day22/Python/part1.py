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
    return [[board[y][x] for y in range(len(board))] for x in range(len(board[0]))]
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
def isValidCoord(board, x, y):
    return x >= 0 and y >= 0 and x < boardWidth(board) and y < boardHeight(board)
def wrapCoords(board, x, y):
    return ((x%boardWidth(board) + boardWidth(board)) % boardWidth(board), (y%boardHeight(board) + boardHeight(board)) % boardHeight(board))

DIR_UP    = 3
DIR_LEFT  = 2
DIR_RIGHT = 0
DIR_DOWN  = 1

moves = {
    DIR_UP:    ( 0,-1),
    DIR_LEFT:  (-1, 0),
    DIR_RIGHT: ( 1, 0),
    DIR_DOWN:  ( 0, 1),
}

left_rot = [DIR_UP, DIR_LEFT, DIR_DOWN, DIR_RIGHT]

def rot_dir(dir, delta):
    return left_rot[((left_rot.index(dir)+delta)%len(left_rot)+len(left_rot))%len(left_rot)]

def move(x, y, dir):
    return (x + moves[dir][0], y + moves[dir][1])

def go_until(board, x, y, dir, do_wrap, cond, before = False):
    dir = rot_dir(dir, 2) # 180
    (nx, ny) = move(x, y, dir)
    if do_wrap:
        (nx, ny) = wrapCoords(board, nx, ny)
    while isValidCoord(board, nx, ny) and not cond(nx, ny):
        (x, y) = (nx, ny)
        (nx, ny) = move(nx, ny, dir)
        if do_wrap:
            (nx, ny) = wrapCoords(board, nx, ny)
    if before:
        return (x, y)
    return (nx, ny)

def day22(contents: str):
    lines = contents.split("\n")
    
    result1 = 0
    result2 = 0

    board = [list(a) for a in lines[:-3]]
    max_width = max(len(a) for a in board)
    for x in board:
        while len(x) < max_width:
            x.append(" ")

    directions = lines[-2]
    board = transpose(board)

    x, y = go_until(board, 0, 0, DIR_LEFT, False, lambda x, y: board[x][y] != " ")
    direction = DIR_RIGHT

    rea = 0
    while rea < len(directions):
        if direction == DIR_UP:
            board[x][y] = "^"
        if direction == DIR_LEFT:
            board[x][y] = "<"
        if direction == DIR_RIGHT:
            board[x][y] = ">"
        if direction == DIR_DOWN:
            board[x][y] = "v"
        if not directions[rea].isnumeric():
            direction = rot_dir(direction, 1 if directions[rea] == "L" else -1)
            rea += 1
        else:
            letter = ""
            while rea < len(directions) and directions[rea].isnumeric():
                letter += directions[rea]
                rea += 1
            size = int(letter)
            for _ in range(size):
                (nx, ny) = move(x, y, direction)
                if not isValidCoord(board, nx, ny) or board[nx][ny] == " ":
                    (nx, ny) = go_until(board, nx, ny, direction, False, lambda x, y: board[x][y] == " ", True)
                if board[nx][ny] == "#":
                    break
                (x, y) = (nx, ny)
                if direction == DIR_UP:
                    board[x][y] = "^"
                if direction == DIR_LEFT:
                    board[x][y] = "<"
                if direction == DIR_RIGHT:
                    board[x][y] = ">"
                if direction == DIR_DOWN:
                    board[x][y] = "v"

    if direction == DIR_UP:
        board[x][y] = "^"
    if direction == DIR_LEFT:
        board[x][y] = "<"
    if direction == DIR_RIGHT:
        board[x][y] = ">"
    if direction == DIR_DOWN:
        board[x][y] = "v"
    printBoard(board)
    print(x, y, direction)
        
    return 1000 * (y+1) + 4 * (x+1) + direction

inputFile = open("../input.txt","r")
print(day22(inputFile.read()))


