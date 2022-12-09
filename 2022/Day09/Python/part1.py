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

poses = set()

def update_tail(tail, head):
    print("a", head, tail)
    w = head[0] - tail[0]
    wd = abs(w) > 1

    ws = 1 if w > 0 else -1
    if w == 0:
        ws = 0

    h = head[1] - tail[1]
    hd = abs(h) > 1

    hs = 1 if h > 0 else -1
    if h == 0:
        hs = 0

    if wd and (head[1] != tail[1]):
        tail[0] += ws
        tail[1] += hs
    elif hd and (head[0] != tail[0]):
        tail[0] += ws
        tail[1] += hs
    elif wd:
        tail[0] += ws
    elif hd:
        tail[1] += hs

    poses.add(tuple(tail))
    print("b", head, tail)
    return wd or hd

def day09(contents: str):
    lines = contents.split("\n")
    
    head = [0, 0]
    tail = [0, 0]
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue
        
        [dir, dist] = l.split(" ")
        dist = int(dist)
        for _ in range(dist):
            if dir == "U":
                head[1] += 1
            if dir == "R":
                head[0] += 1
            if dir == "L":
                head[0] -= 1
            if dir == "D":
                head[1] -= 1
            print(dir)
            print(head, tail)
            while update_tail(tail, head):
                pass
        print("--------------")
    
    return len(poses)

inputFile = open("../input.txt","r")
print(day09(inputFile.read()))


