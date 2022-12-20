from collections.abc import Callable, Iterator
from typing import Any, TypeVar
import pipe as p
import math

T = TypeVar("T")
U = TypeVar("U")

def parseNum(n: str) -> int:
    return int(n.strip().lstrip("+"))

table1 = {

}

table2 = {

}

def day20(contents: str):
    lines = contents.split("\n")
    
    nums = [811589153 * int(l) for l in lines if l != ""]
    indices = list(range(len(nums)))

    for _ in range(10):
        for i in range(len(nums)):
            pos = indices.index(i)

            new_pos = ((pos + nums[i]) % (len(indices)-1)) % (len(indices)-1)
            if new_pos == 0:
                new_pos = len(indices)-1
            # print(nums[i], ":", pos, "->", new_pos)
            indices.pop(pos)
            indices.insert(new_pos, i)
            # print([nums[indices[i]] for i in range(len(indices))])
            # print("--")

    result_list = [nums[indices[i]] for i in range(len(indices))]
    to_get = [1000, 2000, 3000]
    s = 0
    zero_index = result_list.index(0)
    for g in to_get:
        s += result_list[(zero_index + g) % len(result_list)]
    return s

inputFile = open("../input.txt","r")
print(day20(inputFile.read()))


