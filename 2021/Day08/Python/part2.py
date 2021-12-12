
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def day8(contents: str):
    lines = contents.split("\n")

    transcodes = {
        "a": ["a", "b", "c", "d", "e", "f", "g"],
        "b": ["a", "b", "c", "d", "e", "f", "g"],
        "c": ["a", "b", "c", "d", "e", "f", "g"],
        "d": ["a", "b", "c", "d", "e", "f", "g"],
        "e": ["a", "b", "c", "d", "e", "f", "g"],
        "f": ["a", "b", "c", "d", "e", "f", "g"],
        "g": ["a", "b", "c", "d", "e", "f", "g"]
    }

    n = 0
    for line in lines:
        if not ("|" in line):
            continue
        [input, output] = line.split(" | ")
        for digit in output.split(" "):
            p = len(digit)
            if p == 2 or p == 4 or p == 3 or p == 7:
                n += 1
    return n
    """
        for digit in input.split(" "):
            if len(digit) == 2: # 1
                possibilities = ["c", "f"]
                for i in range(len(digit)):
                    transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
            if len(digit) == 4: # 1
                possibilities = ["b", "c", "d", "f"]
                for i in range(len(digit)):
                    transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
            if len(digit) == 2: # 1
                possibilities = ["c", "f"]
                for i in range(len(digit)):
                    transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
            if len(digit) == 2: # 1
                possibilities = ["c", "f"]
                for i in range(len(digit)):
                    transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
    """

    pass

inputFile = open("../input.txt","r")
print(day8(inputFile.read()))


