
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def day13(contents: str):
    [coordinates, folds] = map(lambda g: g.split("\n"), contents.split("\n\n"))
    coordinates = list(map(lambda a: list(map(parseNum, a.split(","))), coordinates))
    folds = folds[:-1]

    size = (0, 0)
    for [x, y] in coordinates:
        if x >= size[0]:
            size = (x+1, size[1])
        if y >= size[1]:
            size = (size[0], y+1)

    matrix = [[False for _ in range(size[1])] for _ in range(size[0])]
    for [x, y] in coordinates:
        matrix[x][y] = True

    def foldY(matrix, fold: int):
        newMatrix = [[False for _ in range(fold+1)] for _ in range(len(matrix))]
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[0])):
                if y == fold:
                    continue
                newY = y if y < fold else fold-abs(y-fold)
                newMatrix[x][newY] = newMatrix[x][newY] or matrix[x][y]
        return newMatrix
    def foldX(matrix, fold: int):
        newMatrix = [[False for _ in range(len(matrix[0]))] for _ in range(fold+1)]
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[0])):
                if x == fold:
                    continue
                newX = x if x < fold else fold-abs(x-fold)
                newMatrix[newX][y] = newMatrix[newX][y] or matrix[x][y]
        return newMatrix

    for i in range(len(folds)):
        [left, right] = folds[i].split("=")
        foldAxis = left[-1]
        foldPos = int(right)

        if foldAxis == "y":
            matrix = foldY(matrix, foldPos)
        elif foldAxis == "x":
            matrix = foldX(matrix, foldPos)
        else:
            print("ERRORRRRR")

        for y in range(0, len(matrix[0])):
            line = ""
            for x in range(0, len(matrix)):
                line += "#" if matrix[x][y] else "."
            print(line)


    c = 0
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if matrix[x][y]:
                c+= 1
    return c


inputFile = open("../input.txt","r")
print(day13(inputFile.read()))


