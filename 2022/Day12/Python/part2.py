from collections.abc import Callable, Iterator
from collections import deque 
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

def day12(contents: str):
    lines = contents.split("\n")
    b = []
    
    startX = 0
    startY = 0
    endX = 0
    endY = 0
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue

        p = []
        for j, x in enumerate(l):
            if x == "S":
                startX = j
                startY = i
                x = "a"
            if x == "E":
                endX = j
                endY = i
                x = "z"
            p.append(x)
        b.append(p)
    
    ls = {}
    q = deque([])
    for x in range(len(b[0])):
        for y in range(len(b)):
            if b[y][x] == "a":
                ls[(x, y)] = 0
                q.append(
                    (b[y][x], [(x, y)], x, y)
                )
    while len(q) > 0:
        (current, path, x, y) = q.popleft()

        if x == endX and y == endY:
            return len(path)-1

        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            px = x + dx
            if px < 0 or px >= len(b[0]):
                continue
            py = y + dy
            if py < 0 or py >= len(b):
                continue

            if not (
                (px, py) not in ls or
                ls[(px, py)] > len(path)+1
            ):
                continue
            diff = ord(b[py][px]) - ord(current)
            if not (
                diff <= 1
            ):
                continue

            ls[(px, py)] = len(path) + 1
            q.append((
                b[py][px],
                path + [(px, py)],
                px, py
            ))
                
            
    

# inputFile = open("../test.txt","r")
inputFile = open("../input.txt","r")
print(day12(inputFile.read()))
