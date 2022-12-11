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

class Monkey:
    def __init__(self, items, op, test, targetT, targetF):
        self.bis = 0
        
        self.items = items
        self.nitems = []
        self.op = op
        self.test = test
        self.targetT = targetT
        self.targetF = targetF

def day11(contents: str):
    lines = contents.split("\n")
    
    mnks = []
    for i in range(0, len(lines), 7):
        l = lines[i]

        its = [int(a) for a in lines[i+1][18:].split(", ") if a != ""]
        m = Monkey(
            its,
            lines[i+2][19:],
            int(lines[i+3][21:]),
            int(lines[i+4][29:]),
            int(lines[i+5][30:]),
        )
        mnks.append(m)

    for r in range(20):
        print(r, "----------------")
        for m in mnks: 
            #print(m.items, m.nitems)
            m.items = m.items + m.nitems
            m.bis += len(m.items)
            for old in m.items:
                print(old)
                new = eval(m.op)
                print(new)
                new = new // 3
                print(new)
                if new % m.test == 0:
                    print("T")
                    print(m.targetT)
                    mnks[m.targetT].nitems.append(new)
                else:
                    print("F")
                    print(m.targetF)
                    mnks[m.targetF].nitems.append(new)
                print("--")
            print(m.items)
            m.items = []
            m.nitems = []

    max_one = max(enumerate(mnks), key = lambda x: x[1].bis)
    mnks.pop(max_one[0])
    max_two = max(enumerate(mnks), key = lambda x: x[1].bis)

    print(max_one[1].bis, max_two[1].bis)
    return max_one[1].bis * max_two[1].bis

inputFile = open("../input.txt","r")
print(day11(inputFile.read()))


