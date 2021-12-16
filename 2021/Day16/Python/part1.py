from collections.abc import Callable
from typing import Any, TypeVar

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
def mapBoard(mm: Callable[[int, int, T], U], board: list[list[T]]) -> list[list[U]]:
    return createBoard(boardWidth(board), boardHeight(board), lambda x, y: mm(x, y, board[x][y]))
def linearBoard(board: list[list[T]]):
    return (
        (
            (x, y, board[x][y])
            for x in range(boardWidth(board))
        )
        for y in range(boardHeight(board))
    )

def parsePacket(packet: str):
    version = int(packet[:3], 2)
    typeId = int(packet[3:6], 2)

    # LITERAL VALUE
    if typeId == 4:
        n = 6
        literal = ""
        while True:
            group = packet[n:(n+5)]
            literal = literal + group[1:]
            n += 5
            if group[0] == "0":
                break
        print("Parsed literal", int(literal, 2))
        return (version, n)
    
    print("Parsing operator packet of version", version)

    totalVersions = version
    n = 6
    if packet[6] == "0":
        subsLength = int(packet[7:22], 2)
        print("Parsing subpackets with lengths", subsLength)
        subs = packet[22:(22+subsLength)]
        n = 0
        while subs[n:] != "" and any(c == "1" for c in subs[n:]):
            print("Parsing sub packet at", n, ":", subs[n:])
            (versions, newPtr) = parsePacket(subs[n:])
            print("Parsed ", versions, ",", newPtr)
            totalVersions += versions
            n += newPtr
        n += 22
    else:
        nbPackets = int(packet[7:18], 2)
        print("Parsing", nbPackets, "subpackets")
        n = 18
        for i in range(nbPackets):
            print("Parsing the #"+str(i))
            (versions, newPtr) = parsePacket(packet[n:])
            totalVersions += versions
            n += newPtr

    print("Finished at", n, "remaining:", packet[n:])
    return (totalVersions, n)

def day16(contents: str):
    print(contents)
    b = ""
    for c in contents[:-1]:
        b += bin(int(c, 16))[2:].zfill(4)
    print(b,"=", len(b))
    print(parsePacket(b))

inputFile = open("../input.txt","r")
print(day16(inputFile.read()))


