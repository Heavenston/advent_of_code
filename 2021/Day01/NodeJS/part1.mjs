import * as fs from "fs";

function day1(numbers) {
    let previous = numbers[0];
    let counter = 0;
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > previous)
            counter++;

        previous = numbers[i];
    }
    return counter;
}

const content = fs.readFileSync("../input.txt", "utf-8");
const numbers = content.split("\n").map(n => parseInt(n)).filter(n => !isNaN(n));

console.log(day1(numbers));
