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

def day07(contents: str):
    lines = contents.split("\n")
    
    dir_stack = []
    dirs = { }
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        
        if l == "":
            continue

        if l[0] == "$":
            args = l.split(" ")
            args.pop(0)
            cmd = args.pop(0)
            if cmd == "cd":
                if args[0] == "/":
                    dir_stack = []
                elif args[0] == "..":
                    dir_stack.pop()
                else:
                    dir_stack.append(args[0])
        else:
            if l.startswith("dir "):
                continue

            size = int(l.split(" ")[0])
            for i in range(1, len(dir_stack)+1):
                dir = "/".join(dir_stack[:i])
                if dir not in dirs:
                    dirs[dir] = 0
                dirs[dir] += size
    
    i = 0
    for k, v in dirs.items():
        print(k, v)
        if v <= 100000:
            i += v
    
    return i

inputFile = open("../input.txt","r")
print(day07(inputFile.read()))


