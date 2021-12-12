
def day3(numbers: list[str]):
    hist: list[list[int]] = [[0,0] for _ in range(len(numbers[0]))]
    for number in numbers:
        for i in range(len(number)):
            hist[i][int(number[i])] += 1

    first = int("".join(["0" if z > o else "1" for [z,o] in hist]), 2)
    second = int("".join(["0" if z <= o else "1" for [z,o] in hist]), 2)
    return first * second

inputFile = open("../input.txt","r")
print(day3(list(
    map(lambda a : a.replace("\n", ""), inputFile.readlines())
)))


