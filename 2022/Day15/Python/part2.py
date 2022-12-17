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

def day15(contents: str):
    lines = contents.split("\n")
    
    cannot_contain = None
   
    sensors = []
    beacons = []

    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue

        [part1, part2] = l.split(":")

        [x1, y1] = part1.split(", ")
        x1 = int(x1[10:].split("=")[1])
        y1 = int(y1.split("=")[1])

        [x2, y2] = part2.split(", ")
        x2 = int(x2[22:].split("=")[1])
        y2 = int(y2.split("=")[1])

        sensors.append((x1, y1, abs(y1 - y2) + abs(x1 - x2)))
        beacons.append((x2, y2))
    
    rows_ranges = [
        [(0, 4000000)] for _ in range(4000000)
    ]
    
    for (sx, sy, dist) in sensors:
        print(sx, sy, dist)
        for i in range(len(rows_ranges)):
            rdist = dist - abs(sy-i)
            if rdist <= 0:
                continue

            x_ranges = rows_ranges[i]
            if x_ranges == None:
                continue

            new_x_ranges = []
            for (rx1, rx2) in x_ranges:
                # If collision
                if rx1 <= sx+rdist and rx2 >= sx-rdist:
                    if sx-rdist-1 >= rx1:
                        new_x_ranges.append((rx1, sx-rdist-1))
                    if rx2 >= sx+rdist+1:
                        new_x_ranges.append((sx+rdist+1, rx2))
                else:
                    new_x_ranges.append((rx1, rx2))

            if new_x_ranges == []:
                rows_ranges[i] = None
            else:
                rows_ranges[i] = new_x_ranges
        print("-------------")

    print([(i, r) for (i, r) in enumerate(rows_ranges) if r != None])
    return "Not found"

inputFile = open("../input.txt","r")
print(day15(inputFile.read()))


