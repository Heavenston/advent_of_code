
def numberParse(s: str):
    return int(s.strip().lstrip("+"))

def day6(contents: str):
    initialFishes = list(map(numberParse, contents.split(",")))

    days = 255
    fishAmount = len(initialFishes)

    agesMap = [0 for _ in range(10)]
    newAgesMap = [0 for _ in range(10)]
    for fish in initialFishes:
        agesMap[fish-1] += 1

    for _ in range(days):
        for i in range(9):
            newAgesMap[i] = agesMap[i+1]

        fishAmount    += agesMap[0]
        newAgesMap[8] += agesMap[0]
        newAgesMap[6] += agesMap[0]

        agesMap = newAgesMap
        newAgesMap = [0 for _ in range(10)]

    return fishAmount

inputFile = open("../input.txt","r")
print(day6(inputFile.read()))


