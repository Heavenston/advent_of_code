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

def day10(contents: str):
    lines = contents.split("\n")
    
    x = 1
    sum = 0
    cycle = 0
    
    screen = [
        [" " for _ in range(40)] for _ in range(6)
    ]
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue
            
        args = l.split(" ")

        if args[0] == "addx":
            cycle += 1
            if x == cycle%40 - 2 or x == cycle%40 - 1 or x == cycle%40:
                screen[cycle//40][cycle%40 - 1] = "#"
            cycle += 1
            if x == cycle%40 - 2 or x == cycle%40 - 1 or x == cycle%40:
                screen[cycle//40][cycle%40 - 1] = "#"
            x += int(args[1])
        elif args[0] == "noop":
            cycle += 1
            if x == cycle%40 - 2 or x == cycle%40 - 1 or x == cycle%40:
                screen[cycle//40][cycle%40 - 1] = "#"
    
    for l in screen:
        for x in l:
            print(x, end="")
        print()

inputFile = open("../input.txt","r")
print(day10(inputFile.read()))


