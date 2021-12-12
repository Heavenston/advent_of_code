
def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def dayX(contents: str):
    pass

inputFile = open("../input.txt","r")
print(dayX(inputFile.read()))


