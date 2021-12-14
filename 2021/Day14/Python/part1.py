from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

"""
Matrixes or Board utils
"""
def boardWidth(board: list[list[str]]) -> int:
    return len(board)
def boardHeight(board: list[list[str]]) -> int:
    return len(board[0])

def parseBoard(text: str):
    map(lambda g: list(g), text.split("\n"))
def createBoard(width: int, height: int, init: Callable[[int, int], T] = (lambda x, y: 0)) -> list[list[T]]:
    return [[init(x, y) for y in range(height)] for x in range(width)]
def printBoard(board: list[list[Any]]):
    for y in range(boardHeight(board)):
        line = ""
        for x in range(boardWidth(board)):
            line += str(board[x][y])
        print(line)
def posIter(board: list[list[Any]]):
    return (
        (x, y)
        for x in range(boardWidth(board))
        for y in range(boardHeight(board))
    )

def day14(contents: str):
    parts = contents.split("\n\n")
    start = parts[0]
    rules = list(map(lambda g: g.split(" -> "), parts[1].split("\n")[:-1]))

    def getL(p: str) -> int:
        l = -1
        for j in range(len(rules)):
            if rules[j][0] == p:
                l = j
                break
        return l

    mappedRules = []
    for [k, v] in rules:
        mappedRules.append([getL(k[0] + v), getL(v + k[1])])
    print(mappedRules)

    def toStr(current: list[int]):
        s = "".join(
            map(
                lambda g: rules[g][0],
                current
            )
        )
        g = s[0] 
        for i in range(1, len(s)-1, 2):
            g += s[i]
            pass
        
        return g + s[-1]

    current: list[int] = []
    for i in range(0, len(start)-1):
        k = start[i]+start[i+1]
        l = -1
        for j in range(len(rules)):
            if rules[j][0] == k:
                l = j
                break
        if l == -1:
            raise Exception("sjdlkfjl")
        current.append(l)

    for p in range(40):
        current = sum(map(lambda l: mappedRules[l], current), [])
        print(p, len(current))
        """
        for i in range(len(current)-2, -1, -1):
            for [k, v] in rules:
                if current[i] == k[0] and current[i+1] == k[1]:
                    current.insert(i, v)
        """

    s = toStr(current)
    p = [0 for _ in range(256)]
    for c in s:
        p[ord(c)] += 1

    print(sum(p))
    print("max: ", max(p))
    print("min: ", min(filter(lambda l: l != 0, p)))

    return max(p) - min(filter(lambda l: l != 0, p))

inputFile = open("../test.txt","r")
print(day14(inputFile.read()))


