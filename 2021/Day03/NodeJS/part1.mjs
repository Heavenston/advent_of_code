import * as fs from "fs";

function day3(numbers) {
    const hist = new Array(numbers[0].length).fill(null).map(_ => [0,0]);
    numbers
        .forEach(number => {
            [...number].forEach((d, i) => hist[i][+d]++);
        });

    return parseInt(hist.map(([z, o]) => z > o ? "0" : "1").join(""), 2)
         * parseInt(hist.map(([z, o]) => z > o ? "1" : "0").join(""), 2)
}

const content = fs.readFileSync("../input.txt", "utf-8");
console.log(day3(content.split("\n")));

