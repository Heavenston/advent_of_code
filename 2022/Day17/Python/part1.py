from collections.abc import Callable, Iterator
from typing import Any, TypeVar
import pipe as p
import math

T = TypeVar("T")
U = TypeVar("U")

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

table1 = {

}

table2 = {

}

rocks = [
   ["####"],

   [".#.",
    "###",
    ".#."],

   ["..#",
    "..#",
    "###"],

   ["#",
    "#",
    "#",
    "#"],

   ["##",
    "##"]
]

boardWidth = 7

def printBoard(board):
    print("---------")
    for line in reversed(board):
        print("".join(line))
    print("---------")

def collides(rock, posx, posy, board):
    if posx > boardWidth - len(rock[0]):
        return True
    if posx < 0:
        return True
    if posy < len(rock)-1:
        return True;

    for dy in range(len(rock)):
        if posy-dy >= len(board):
            continue
        for dx in range(len(rock[0])):
            if board[posy-dy][posx+dx] != "." and rock[dy][dx] != ".":
                return True
    return False

def day17(contents: str):
    lines = contents.split("\n")
    
    board = []
    moves = lines[0]

    rockc = 0
    movec = 0

    for i in range(2022):
        print(i)
        rock = rocks[rockc]
        rockc += 1
        rockc = rockc % len(rocks)
        print(rock)

        posx = 2
        posy = len(board) + 2 + len(rock)

        while True:
            move = moves[movec]
            movec += 1
            movec = movec % len(moves)

            if move == ">":
                posx += 1
                if collides(rock, posx, posy, board):
                    posx -= 1
                # else:
                #     print(move)
            elif move == "<":
                posx -= 1
                if collides(rock, posx, posy, board):
                    posx += 1
                # else:
                #     print(move)

            posy -= 1
            if collides(rock, posx, posy, board):
                posy += 1
                while len(board) <= posy:
                    board.append(["." for _ in range(boardWidth)])
                for dy in range(len(rock)):
                    for dx in range(len(rock[0])):
                        if rock[dy][dx] != ".":
                            board[posy-dy][posx+dx] = "#"
                # print("Place at", posx, posy)
                # printBoard(board)

                break
    return len(board)

inputFile = open("../input.txt","r")
print(day17(inputFile.read()))


