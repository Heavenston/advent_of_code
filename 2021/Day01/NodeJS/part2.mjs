import * as fs from "fs";

function day1(numbers) {
    const getWindow = (i, size = 3) => {
        let total = 0;
        for (let d = 0; d < size; d++)
            total += numbers[i + d];
        return total;
    };

    let previous = getWindow(0);
    let counter = 0;
    for (let i = 1; i < numbers.length; i++) {
        const current = getWindow(i);
        if (current > previous)
            counter++;

        previous = current;
    }

    console.log(counter);
}

const content = fs.readFileSync("../input.txt", "utf-8");
const numbers = content.split("\n").map(n => parseInt(n)).filter(n => !isNaN(n));

console.log(day1(numbers));
