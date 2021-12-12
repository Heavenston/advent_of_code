from collections.abc import Callable

def day3(numbers: list[str]):
    def getNumber(compare: Callable[[int, int], str]):
        i = 0
        result: list[str] = list(numbers)
        while len(result) > 1:
            expected = compare(
                sum(x[i] == "0" for x in result),
                sum(x[i] == "1" for x in result)
            )
            result = list(filter(
                lambda n: n[i] == expected,
                result
            ))
            i += 1
        return int(result[0], 2)

    return getNumber(lambda z, o: "0" if z > o else "1") * getNumber(lambda z, o: "1" if z > o else "0")

inputFile = open("../input.txt","r")
print(day3(list(
    map(lambda a : a.replace("\n", ""), inputFile.readlines())
)))


