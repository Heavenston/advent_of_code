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

def compare(a, b):
    la = isinstance(a, list)
    lb = isinstance(b, list)
    if la and lb:
        for i in range(min(len(a), len(b))):
            x = compare(a[i], b[i])
            if x != 0:
                return x
        return len(a) - len(b)
    elif la:
        return compare(a, [b])
    elif lb:
        return compare([a], b)
    else:
        return b - a


def day13(contents: str):
    lines = contents.split("\n")
    
    result1 = 0
    result2 = 0
    
    ls = [[[2]], [[6]]]
    for i in range(0, len(lines), 3):
        l1 = eval(lines[i])
        l2 = eval(lines[i+1])
        ls.append(l1)
        ls.append(l2)
    ls.sort(key=lambda a: compare(0, a))
    first = 0
    second = 0
    for i, x in enumerate(ls):
        if x == [[2]]:
            first = i+1
        if x == [[6]]:
            second = i+1
        continue
        print(x)
        if isinstance(x, list):
            print("a")
            if len(x) == 1 and isinstance(x[0], list):
                if len(x[0]) == 1 and x[0][0] == 2:
                    first = i+1
                if len(x[0]) == 1 and x[0][0] == 6:
                    second = i+1
    
    return first * second

inputFile = open("../input.txt","r")
print(day13(inputFile.read()))


