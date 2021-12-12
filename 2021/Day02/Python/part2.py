
def day2(lines: list[str]):
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        [action, param] = line.split(" ")
        x = int(param)
        if action == "forward":
            horizontal += x
            depth += aim * x
        elif action == "down":
            aim += x
        elif action == "up":
            aim -= x
    return horizontal * depth

inputFile = open("../input.txt","r")
print(day2(inputFile.readlines()))


