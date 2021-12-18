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

def getMost(el, pos: int):
    if type(el) == int:
        return el
    if type(el) == list:
        return getMost(el[pos], pos)
def getAndAdd(el, pos: int, add: int):
    if type(el) == int:
        return el+add
    if type(el) == list:
        el[pos] = getAndAdd(el[pos], pos, add)
        return el

def simplify(el, step: str, depth: int = 0):
    if type(el) == int and step == "split":
        if el >= 10:
            # print("Spliting of", el)
            el = [math.floor(el / 2), math.ceil(el / 2)]
            return True, el, (-1, -1)
        return False, el, (-1, -1)

    if depth == 4 and type(el) == list and step == "explode":
        # print("Explosion of", el)
        return True, 0, (el[0], el[1])
    
    if type(el) == list:
        action, el[0], explosions = simplify(el[0], step, depth+1)
        if explosions[1] != -1:
            el[1] = getAndAdd(el[1], 0, explosions[1])
            explosions = (explosions[0], -1)
        if action:
            return True, el, explosions

        action, el[1], explosions = simplify(el[1], step, depth+1)
        if explosions[0] != -1:
            el[0] = getAndAdd(el[0], -1, explosions[0])
            explosions = (-1, explosions[1])
        if action:
            return True, el, explosions

    return (False, el, (-1, -1))

def magn(a):
    if type(a) == int:
        return a
    return 3 * magn(a[0]) + 2 * magn(a[1])


def day18(contents: str):
    toAdd = []
    for c in contents.split("\n")[:-1]:
        toAdd.append(eval(c))

    el = toAdd[0]
    for a in toAdd[1:]:
        print(el, "+", a)
        el = [el, a]
        didSomething = True
        while didSomething:
            didSomething, el, _ = simplify(el, "explode")
            if not didSomething:
                didSomething, el, _ = simplify(el, "split")
            print("Step", el)
        print("=", el)
        print()

    return magn(el)

inputFile = open("../input.txt","r")
print(day18(inputFile.read()))


