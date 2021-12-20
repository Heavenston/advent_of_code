from collections.abc import Callable, Iterator
from typing import Any, TypeVar
from itertools import permutations
import transformations as trsfms
import pipe as p
import numpy as np
import math
import pickle

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

## qghytfvbnjuytfvbjuytfvbnjuèytfvbhytrf

def applyTransformation(pos, trans):
    (negs, posPerm, delta) = trans
    return [pos[posPerm[i]]*negs[i] + delta[i] for i in range(3)]

def compositTransform(first, second):
    (negs1, posPerm1, delta1) = first
    (negs2, posPerm2, delta2) = second
    return (
        [negs1[posPerm2[i]] * negs2[i] for i in range(3)],
        [posPerm2[posPerm1[i]] for i in range(3)],
        applyTransformation(delta1, second)
    )

def transMatrix(v):
    return np.ndarray((4, 4), dtype = int,
            buffer = np.array([1, 0, 0, v[0],
                               0, 1, 0, v[1],
                               0, 0, 1, v[2],
                               0, 0, 0, 1    ]))

class Scanner:
    def __init__(self, beaconsRelative, index: int):
        self.absoluteTransform = None

        self.index = index
        self.beaconsRelative = beaconsRelative

    def relativePosOf(self, other):
        found = None
        for negs in [[int(p)*2 - 1 for p in bin(n)[2:].zfill(3)] for n in range(7, -1, -1)]:
            for posPerm in permutations([0, 1, 2]):
                trns = np.ndarray((4, 4), dtype = int,
                        buffer = np.array([0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 0,
                                           0, 0, 0, 1]))
                for x in range(0, 3):
                    for y in range(0, 3):
                        trns[x, y] = int(posPerm[x] == y) * negs[x]
                ffids = (
                    np.matmul(
                        trns,
                        [b2[0], b2[1], b2[2], 1]
                    ) + [b1[0], b1[1], b1[2], 0]

                    for b1 in self.beaconsRelative
                    for b2 in other.beaconsRelative
                )
                diffs = [
                    (a, sum(a[i] ** (i+2) for i in range(len(a))))
                    for a in ffids
                ]
                eq = {}
                for i in range(len(diffs)):
                    for j in range(len(diffs)):
                        if i == j:
                            continue
                        (a, dist) = diffs[i]
                        (_, dist2) = diffs[j]
                        if dist != dist2:
                            continue
                        if dist not in eq:
                            eq[dist] = []
                        eq[dist].append(a)
                if len(eq) == 0:
                    continue
                best = max(eq.keys(), key = lambda k: len(eq[k]))
                if len(eq[best]) >= 12:
                    found = np.matmul(
                        transMatrix(eq[best][0]),
                        trns,
                    )
                    break
            else:
                continue
            break

        return found

    def updateAbsolutePos(self, absolute, relativeToAbs):
        self.absoluteTransform = np.matmul(absolute, relativeToAbs);

def generate():
    inputFile = open("../test.txt","r")
    contents = inputFile.read()

    scanners = []

    i = 0
    for scannerText in contents.split("\n\n"):
        beacons = list(map(lambda p: list(parseNum(n) for n in p.split(",")), scannerText.split("\n")[1:-1]))
        scanner = Scanner(beacons, i)
        scanners.append(scanner)
        i += 1

    scanners[0].absoluteTransform = np.identity(4)
    
    done = set()
    for scanner in scanners:
        for scanner2 in scanners:
            if scanner == scanner2 or ((scanner.index, scanner2.index) in done):
                continue
            done.add((scanner.index, scanner2.index))
            done.add((scanner2.index, scanner.index))
            print(scanner.index, "vs", scanner2.index)

            result = scanner.relativePosOf(scanner2)
            print("->", result)
            if result is not None:
                if scanner.absoluteTransform is not None and scanner2.absoluteTransform is None:
                    scanner2.updateAbsolutePos(scanner.absoluteTransform, result)
                elif scanner2.absoluteTransform is not None and scanner.absoluteTransform is None:
                    scanner.updateAbsolutePos(scanner.absoluteTransform, result)
                print("Their absolute poses are now:")
                print(scanner.index, "\n", scanner.absoluteTransform.astype(np.int32))
                print(scanner2.index, "\n", scanner2.absoluteTransform.astype(np.int32))

    print("------------ OPEN -----------")
    for scanner in scanners:
        print(scanner.index, "\n", scanner.absoluteTransform.astype(np.int32))
        
    
    with open("scanners.pkl", "wb") as fi:
        pickle.dump(scanners, fi)

def test():
    with open("scanners.pkl", "rb") as fi:
        scanners = pickle.load(fi)

    beacons = set()

    for scanner in scanners:
        for [x, y, z] in scanner.beaconsRelative:
            [gx, gy, gz, _] = list(map(int, np.matmul(scanner.absoluteTransform, [x, y, z, 1])))
            print(gx, gy, gz)
            beacons.add((gx, gy, gz))

    print(len(beacons))

generate()


