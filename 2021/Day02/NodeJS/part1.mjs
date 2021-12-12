import * as fs from "fs";

function day2(lines) {
    let horizontal = 0;
    let depth = 0;
    for (const line of lines) {
        const [action, param] = line.split(" ");
        const x = parseInt(param);
        if (action == "forward")
            horizontal += x;
        else if (action == "down")
            depth += x;
        else if (action == "up")
            depth -= x;
    }
    return horizontal * depth;
}

const content = fs.readFileSync("../input.txt", "utf-8");
console.log(day2(content.split("\n")));

