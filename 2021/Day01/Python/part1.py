def day1(numbers):
    return sum([
        numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)
    ])

inputFile = open("../input.txt","r")
numbers = [int(line.replace("\n", "")) for line in inputFile.readlines()]

print(day1(numbers))


