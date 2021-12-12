
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

    def continuePath(path: list[Cave], didVisitTwice: bool = False):
        paths = []
        for cave in path[-1].connectedTo:
            if cave.name == "start":
                continue
            if didVisitTwice and not cave.isBig and cave in path:
                continue
            if cave.name == "end":
                paths.append(path)
                continue
            newPath = list(path)
            newPath.append(cave)
            paths += continuePath(newPath, didVisitTwice or (cave in path and not cave.isBig))
        return paths

    h = continuePath([nodes["start"]])

    print(len(h))


inputFile = open("input.txt","r")
print(day12(inputFile.read()))


