
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

openToClose = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def day10(contents: str):

    s = 0
    for line in contents.split("\n"):
        errorScore = 0
        openStack = []
        for c in line:
            if c in openToClose.keys():
                openStack.append(c)
            else:
                if openToClose[openStack[-1]] == c: # If the right closing
                    openStack.pop()
                else:
                    errorScore = points[c]
                    print("Error, expected "+openToClose[openStack[-1]]+" but found "+c+" points:"+str(errorScore))
                    break

        s += errorScore

    return s

inputFile = open("../input.txt","r")
print(day10(inputFile.read()))


