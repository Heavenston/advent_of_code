
class Cave:
    def __init__(self, name: str):
        self.isBig = name.isupper()
        self.name = name.lower()
        self.connectedTo = set()

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

def day12(contents: str):
    nodes: dict[str, Cave] = {}
    for line in contents.split("\n"):
        if line == "":
            continue
        [a, b] = line.split("-")
        if a not in nodes:
            nodes[a] = Cave(a)
        if b not in nodes:
            nodes[b] = Cave(b)
        nodes[a].connectedTo.add(nodes[b])
        nodes[b].connectedTo.add(nodes[a])

    def continuePath(path: list[Cave]):
        count = 0
        for cave in path[-1].connectedTo:
            if cave in path and not cave.isBig:
                continue
            if cave.name == "end":
                count += 1
                continue
            newPath = list(path)
            newPath.append(cave)
            count += continuePath(newPath)
        return count

    return continuePath([nodes["start"]])


inputFile = open("input.txt","r")
print(day12(inputFile.read()))


