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

def ev(values, name):
    if not isinstance(values[name], str):
        return values[name]

    [a, op, b] = values[name].split(" ")
    av = ev(values, a)
    bv = ev(values, b)
    return eval(values[name], None, {
        a: av, b: bv
    })

def to_str(values, name):
    if not isinstance(values[name], str):
        return str(values[name])

    [a, op, b] = values[name].split(" ")
    av = to_str(values, a)
    bv = to_str(values, b)
    return "(" + av + " " + op + " " + bv + ")"

def extend_poly(h, size):
    while len(h) < size:
        h.append(0)
        h.insert(0, 0)

def to_poly(values, name):
    if not isinstance(values[name], str):
        if name == "humn":
            return [1, 0, 0]
        return [float(values[name])]

    [a, op, b] = values[name].split(" ")
    ap = to_poly(values, a)
    bp = to_poly(values, b)

    if op == "+":
        extend_poly(ap, len(bp))
        extend_poly(bp, len(ap))
        for i in range(len(bp)):
            ap[i] += bp[i]
        out = ap
    if op == "-":
        extend_poly(ap, len(bp))
        extend_poly(bp, len(ap))
        for i in range(len(bp)):
            ap[i] -= bp[i]
        out = ap
    if op == "*":
        out = [0] * (len(ap) + len(bp) - 1)
        for i in range(len(ap)):
            for j in range(len(bp)):
                 out[i+j] += ap[i] * bp[j]
    if op == "/":
        for i in range(len(bp)//2):
            (bp[i], bp[-i-1]) = (bp[-i-1], bp[i])

        out = [0] * (len(ap) + len(bp) - 1)
        for i in range(len(ap)):
            for j in range(len(bp)):
                 out[i+j] += ap[i] / bp[j]

    return out
                

def day21(contents: str):
    lines = contents.split("\n")
    
    values = {}
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue

        [name, op] = l.split(": ")
        if op.isnumeric():
            values[name] = int(op)
        else:
            if name == "root":
                op = op.replace("+", "-")
            values[name] = op
   
    poly = to_poly(values, "root")
    print("Equivalent to poly", poly)

    print("Value with x = 0")
    values["humn"] = 0
    print("  Poly  says:", poly[1])
    print("  Part1 says:", ev(values, "root"))
    for x in range(4):
        print("Value with x = "+str(x))
        values["humn"] = x
        print("  Poly  says:", poly[1] + x*poly[0])
        print("  Part1 says:", ev(values, "root"))

    return (-poly[1]) / poly[0]

inputFile = open("../input.txt","r")
print(day21(inputFile.read()))


