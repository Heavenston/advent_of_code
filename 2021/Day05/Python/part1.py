
def parsePos(t: str):
    [x, y] = t.split(",")
    return (int(x), int(y))

def day5(lines: list[str]):
    size = 1000
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for vent in lines:
        [(x1, y1), (x2, y2)] = map(parsePos, vent.split(" -> "))
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid[x][y] += 1

    count = 0
    for x in range(0, size):
        for y in range(0, size):
            if grid[x][y] >= 2:
                count += 1

    return count


inputFile = open("../input.txt","r")
print(day5(inputFile.readlines()))


