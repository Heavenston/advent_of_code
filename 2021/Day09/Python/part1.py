
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def dayX(contents: str):
    lines = contents.split("\n")[:-1]
    board = list(map(lambda a: list(map(parseNum, list(a))), lines))

    height = len(lines)
    width = len(lines[0])

    s = 0
    for y in range(height):
        for x in range(width):
            n = board[y][x]
            isLow = all(
                board[y+dy][x+dx] > n for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)] if x+dx >= 0 and x+dx < width and y+dy >= 0 and y+dy < height
            )

            if isLow:
                s += n+1

    return s


inputFile = open("../input.txt","r")
print(dayX(inputFile.read()))


