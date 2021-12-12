
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def day7(contents: str):
    numbers = list(map(parseNum, contents.split(",")))

    decidedH = sum(numbers) // len(numbers)
    print(decidedH)

    least = 9999999999
    for i in range(1000):
        s = 0
        for n in numbers:
            j = abs(n-i)
            s += (j * (j+1)) / 2
        if s < least:
            least = s
    return least

inputFile = open("../input.txt","r")
print(day7(inputFile.read()))

