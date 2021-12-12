
offsets_neighbors = [(1, 0),(0, 1),(-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))


def day11(contents: str):
    octopuses: list[list[int]] = list(map(lambda g: list(map(parseNum, list(g))), contents.split("\n")[:-1]))
    width = len(octopuses[0])
    height = len(octopuses)

    def show():
        print("-----------------------------------")
        for y in range(height):
            print(octopuses[y])

    def neigbors(x: int, y: int):
        return filter(
            lambda pos: pos[0] >= 0 and pos[1] >= 0 and pos[0] < width and pos[1] < height,
            map(
                lambda d: (x + d[0], y + d[1]),
                offsets_neighbors
            )
        )

    def flash_step():
        lastFlashes = 1
        totalFlashes = 0
        increased: set[tuple[int, int]] = set()
        while lastFlashes > 0:
            lastFlashes = 0
            for x in range(width):
                for y in range(height):
                    if octopuses[y][x] > 9 and (x, y) not in increased:
                        increased.add((x, y))

                        octopuses[y][x] = 0
                        for (nx, ny) in neigbors(x, y):
                            if (nx, ny) not in increased:
                                octopuses[ny][nx] += 1

                        totalFlashes += 1
                        lastFlashes += 1
        return totalFlashes

    def step():
        for x in range(width):
            for y in range(height):
                octopuses[y][x] += 1
        return flash_step()

    flashes = 0
    for _ in range(100):
        flashes += step()

    print(flashes)

inputFile = open("input.txt","r")
print(day11(inputFile.read()))


