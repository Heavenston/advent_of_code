
def parsePos(t: str):
    [x, y] = t.split(",")
    return (int(x), int(y))

def day5(lines: list[str]):
    size = 1000
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for vent in lines:
        [(x1, y1), (x2, y2)] = map(parsePos, vent.split(" -> "))
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[x][y] += 1
        else:
            xOffset = 0
            xOffsetDir = 1 if x2 > x1 else -1
            yOffset = 0
            yOffsetDir = 1 if y2 > y1 else -1
            print(x1, y1, x2, y2)
            while x1 + xOffset != x2:
                grid[x1 + xOffset][y1 + yOffset] += 1
                xOffset += xOffsetDir
                yOffset += yOffsetDir
            grid[x1 + xOffset][y1 + yOffset] += 1

    count = 0
    for x in range(0, size):
        for y in range(0, size):
            if grid[x][y] >= 2:
                count += 1

    return count


inputFile = open("../input.txt","r")
print(day5(inputFile.readlines()))


