
def numberParse(s: str):
    return int(s.strip().lstrip("+"))

def day6(contents: str):
    fishes = list(map(numberParse, contents.split(",")))
    newFishes = []

    for _ in range(80):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                newFishes.append(8)
                fishes[i] = 6
            else:
                fishes[i] -= 1
        fishes.extend(newFishes)
        newFishes = []

    return len(fishes)

inputFile = open("../test.txt","r")
print(day6(inputFile.read()))


