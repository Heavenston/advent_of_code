def day2(lines: list[str]):
    horizontal = 0
    depth = 0
    for line in lines:
        [action, param] = line.split(" ")
        x = int(param)
        if action == "forward":
            horizontal += x
        elif action == "down":
            depth += x
        elif action == "up":
            depth -= x
    return horizontal * depth

inputFile = open("../input.txt","r")
print(day2(inputFile.readlines()))


