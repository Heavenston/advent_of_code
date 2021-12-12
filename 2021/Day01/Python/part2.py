def day1(numbers):
    windows = [
        numbers[i] + numbers[i + 1] + numbers[i + 2] for i in range(len(numbers) - 2)
    ]
    return sum([
        windows[i] < windows[i + 1] for i in range(len(windows) - 1)
    ])

inputFile = open("../input.txt","r")
numbers = [int(line.replace("\n", "")) for line in inputFile.readlines()]

print(day1(numbers))


