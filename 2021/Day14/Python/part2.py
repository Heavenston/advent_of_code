from collections.abc import Callable
from typing import Any, TypeVar
import math

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

    """
    dubbleMappedRules = [[mappedRules[i]] for i in range(len(mappedRules))]
    for _ in range(10):
        for i in range(len(mappedRules)):
            dubbleMappedRules[i].append(list(dubbleMappedRules[i][-1]))
            for l in dubbleMappedRules[i][-1]:
                dubbleMappedRules[i][-1].append(mappedRules[l][0])
                dubbleMappedRules[i][-1].append(mappedRules[l][1])
    print(dubbleMappedRules[0])
    """

    def toStr(currentHist: list[int]):
        s = "".join(
            rules[i][0] * (currentHist[i])
            for i in range(len(currentHist))
        )
        g = ""
        for i in range(0, len(s), 2):
            g += s[i]
            pass
        
        return s

    currentHist = [0 for _ in range(len(rules))]
    for i in range(0, len(start)-1):
        k = start[i]+start[i+1]
        l = -1
        for j in range(len(rules)):
            if rules[j][0] == k:
                l = j
                break
        if l == -1:
            raise Exception("sjdlkfjl")
        currentHist[l] += 1

    for p in range(40):
        newHist = [0 for _ in range(len(rules))]
        for l in range(len(rules)):
            newHist[mappedRules[l][0]] += currentHist[l]
            newHist[mappedRules[l][1]] += currentHist[l]
        currentHist = newHist
        # current = sum(map(lambda l: mappedRules[l], current), [])
        # print(len(current))
        """
        for i in range(len(current)-2, -1, -1):
            for [k, v] in rules:
                if current[i] == k[0] and current[i+1] == k[1]:
                    current.insert(i, v)
        """

    p = [0 for _ in range(256)]
    for i in range(len(currentHist)):
        p[ord(rules[i][0][0])] += currentHist[i]
        p[ord(rules[i][0][1])] += currentHist[i] 

    print(sum(p))
    print("max: ", max(p))
    print("min: ", min(filter(lambda l: l != 0, p)))

    return (max(p) - min(filter(lambda l: l != 0, p))) // 2 + 1

inputFile = open("../input.txt","r")
print(day14(inputFile.read()))


