
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def dayX(contents: str):
    lines = contents.split("\n")[:-1]
    board = list(map(lambda a: list(map(parseNum, list(a))), lines))

    height = len(board)
    width = len(board[0])
    print("width:", width)
    print("height:", height)

    checked: set[tuple[int, int]] = set()

    basins = []
    for y in range(height):
        for x in range(width):
            if (x, y) in checked:
                continue
            n = board[y][x]
            isLow = all(
                board[y+dy][x+dx] > n
                for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]
                if x+dx >= 0 and x+dx < width and y+dy >= 0 and y+dy < height
            )
            print("----------", n, "------------", list(
                board[y+dy][x+dx] > n
                for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]
                if x+dx >= 0 and x+dx < width and y+dy >= 0 and y+dy < height
            ))
            if not isLow:
                continue

            # print("-----------------------------------------");
            # print(x, y, "is low")
            basinSize = 0
            toCheck = [(x, y)]
            while toCheck != []:
                i, j = toCheck.pop()
                # print("---- ", x, y)
                if (i, j) in checked:
                    continue
                # print(board)
                # print(p, "=", board[p[1]][p[0]])
                checked.add((i, j))
                basinSize += 1
                toCheck.extend(
                    (i+dx, j+dy) for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]
                    # if x+dx >= 0 and x+dx < width and y+dy >= 0 and y+dy < height
                    if (i+dx, j+dy) not in checked and i+dx >= 0 and i+dx < width and j+dy >= 0 and j+dy < height and board[j+dy][i+dx] != 9
                )
                # print(toCheck)
            #print("Bassin Size: ", basinSize)
            basins.append(basinSize)

    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


inputFile = open("../input.txt","r")
print(dayX(inputFile.read()))


