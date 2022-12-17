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

    cache = {}
    
    board = []
    moves = lines[0]

    rockc = 0
    movec = 0

    target_t = 1000000000000
    added_height = 0
    i = 0

    while i < target_t:
        if i > 0 and added_height == 0:
            key = (tuple(tuple(a) for a in board[-50:]), rockc, movec)
            if key in cache:
                v = cache[key]
                loop_height = len(board) - v[1]
                print("Loop Height", loop_height)
                loop_duration = i - v[0]
                print("     Duration", loop_duration)
                loop_start = v[0]
                print("     Start Time", loop_start)
                height_at_loop = v[1]
                print("     Start Height", height_at_loop)

                blocks = (target_t - loop_start) // loop_duration
                added_height = (blocks - 1) * loop_height
                i = blocks * loop_duration + loop_start
            cache[key] = (i, len(board))

        rock = rocks[rockc]
        rockc += 1
        rockc = rockc % len(rocks)

        posx = 2
        posy = len(board) + 2 + len(rock)

        start_height = len(board)
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

        i += 1
    return len(board) + added_height

inputFile = open("../input.txt","r")
print(day17(inputFile.read()))


