
ORE      = 0
CLAY     = 1
OBSIDIAN = 2
GEODE    = 3

names = {
    "ore": ORE,
    "clay": CLAY,
    "obsidian": OBSIDIAN,
    "geode": GEODE,
}

def score(b):
    return tuple(reversed(b))

def blueprint_score(blueprint, iterations):

    worlds = {
        (1, 0, 0, 0): set([(0, 0, 0, 0)])
    }

    for i in range(iterations):
        # print("ITERATION  ", i)
        # print("WORLD COUNT", sum(len(w) for w in worlds.values()))

        new_worlds = {}
        world_overwrites = {}
        for robots, resources_list in worlds.items():
            new_resources_list  = set()
            for resources in resources_list:
                can_craft = []
                for i, r in enumerate(blueprint):
                    if all(a >= b for a, b in zip(resources, r)):
                        can_craft.append(i)

                resources = tuple(a + b for a, b in zip(resources, robots))
                new_resources_list.add(resources)

                # Splitting the universe
                if can_craft != []:
                    for cc in can_craft:
                        rbts = tuple(a + (1 if i == cc else 0) for i, a in enumerate(robots))
                        rsrs = tuple(a - b for a, b in zip(resources, blueprint[cc]))
                        if rbts not in world_overwrites:
                            world_overwrites[rbts] = set()
                        world_overwrites[rbts].add(rsrs)
            new_worlds[robots] = new_resources_list

            # print("| Robots:   ", robots)
            # print("| Resources:", resources)
            # print("-" * 10)

        worlds = new_worlds
        for k, v in world_overwrites.items():
            if k not in worlds:
                worlds[k] = set()
            for m in v:
                worlds[k].add(m)
        for k in worlds.keys():
            # Pruning to the best 10
            worlds[k] = set(sorted(list(worlds[k]), key = score, reverse = True)[:10])

    return max(b[GEODE] for a in worlds.values() for b in a)

def day19(contents: str):
    lines = contents.split("\n")

    blueprints = []
    
    for i in range(0, len(lines), 1):
        l = lines[i]
        if l == "":
            continue

        [part1, *parts] = l.split(". ")
        part1 = part1.split(":")[1].strip()

        costs = [
            [word for word in part.split(" ")[4:] if word != "and"]
            for part in [part1, *parts]
        ]

        for i in range(len(costs)):
            c = costs[i]
            costs[i] = [0] * 4
            for k, v in zip((names[i.strip(".")] for i in c[1::2]), c[0::2]):
                costs[i][k] = int(v)

        blueprints.append(costs)

    print("Blueprints:", blueprints)
    print("-" * 40)

    s = 1
    for i, bl in enumerate(blueprints[:3]):
        score = blueprint_score(bl, 32)
        print("Blueprint", i, "has score", score)
        s *= score
    return s
    

inputFile = open("../input.txt","r")
print(day19(inputFile.read()))


