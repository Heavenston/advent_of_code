
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

openToClose = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}
points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def day10(contents: str):

    scores = []
    for line in contents.split("\n"):
        errored = False
        openStack = []
        for c in line:
            if c in openToClose.keys():
                openStack.append(c)
            else:
                if openToClose[openStack[-1]] == c: # If the right closing
                    openStack.pop()
                else:
                    print("Error, expected "+openToClose[openStack[-1]]+" but found "+c)
                    errored = True
                    break
        if errored:
            continue

        s = 0
        for l in reversed(openStack):
            s *= 5
            s += points[openToClose[l]]
        scores.append(s)

    scs = sorted(scores)
    return scs[int(len(scs)/2)]

inputFile = open("../input.txt","r")
print(day10(inputFile.read()))


