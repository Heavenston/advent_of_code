
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def day8(contents: str):
    lines = contents.split("\n")

    numbers = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]

    total = 0
    for line in lines:
        if not ("|" in line):
            continue
        transcodes = {
            "a": ["a", "b", "c", "d", "e", "f", "g"],
            "b": ["a", "b", "c", "d", "e", "f", "g"],
            "c": ["a", "b", "c", "d", "e", "f", "g"],
            "d": ["a", "b", "c", "d", "e", "f", "g"],
            "e": ["a", "b", "c", "d", "e", "f", "g"],
            "f": ["a", "b", "c", "d", "e", "f", "g"],
            "g": ["a", "b", "c", "d", "e", "f", "g"]
        }

        def whatCanItBe(d: str) -> set[str]:
            poss = filter(lambda g: len(g) == len(d), numbers)
            t = []
            for c in d:
                t += transcodes[c]
            poss = filter(lambda p: all(map(lambda g: (g in t), p)), poss)
            return set(poss)

        [input, output] = line.split(" | ")
        for _ in range(10):
            for digit in input.split(" "):
                hmm = whatCanItBe(digit)
                # print("----------------------------------------------------------------------------------------------------------------------------------------------")
                # print(transcodes)
                # print(digit, "->", hmm)
                possibilities = [item for sublist in hmm for item in sublist]
                for l in digit:
                    transcodes[l] = list(filter(lambda x: x in possibilities, transcodes[l]))
                for l in set(transcodes.keys()) - set(digit):
                    transcodes[l] = list(filter(lambda x: not all(map(lambda y: x in y, hmm)), transcodes[l]))
                # print(digit, set(transcodes.keys()) - set(digit))
                # print(transcodes)
                """
                if len(digit) == 2: # 1
                    possibilities = ["c", "f"]
                    for i in range(len(digit)):
                        transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
                if len(digit) == 4: # 1
                    possibilities = ["b", "c", "d", "f"]
                    for i in range(len(digit)):
                        transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
                if len(digit) == 5: # 2 3 5
                    possibilities = ["b", "c", "d", "f"]
                    for i in range(len(digit)):
                        transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
                if len(digit) == 3: # 1
                    possibilities = ["a", "c", "f"]
                    for i in range(len(digit)):
                        transcodes[digit[i]] = list(filter(lambda x: x in possibilities, transcodes[digit[i]]))
                """

        print(transcodes)
        decodedOutput = []
        for o in output.split(" "):
            n = ""
            for l in o:
                n += transcodes[l][0]
            decodedOutput.append(set(n))
        nnn = list(map(set, numbers))
        resultDigits = list(map(nnn.index, decodedOutput))

        r = 0
        for l in resultDigits:
            r *= 10
            r += l
        total += r


    return total

inputFile = open("../input.txt","r")
print(day8(inputFile.read()))


