import * as fs from "fs";

const calibrateDuplicates = (input) => {
  let breakdown = input
    .split('\n')
    .map(x => parseInt(x.trim().replace("+", ""), 10))
    .filter(a => !isNaN(a));
  
  let currentFrequency = 0, i = 0;
  let duplicateFound = false;
  let pastFrequencies = [currentFrequency];

  while(!duplicateFound) {
    
    if (i === breakdown.length) { i = 0; };
    
    currentFrequency += breakdown[i];
    
    duplicateFound = pastFrequencies.includes(currentFrequency);
    
    pastFrequencies.push(currentFrequency);
    
    i++;
  }

  return currentFrequency;
};

const content = fs.readFileSync("../day1.txt", "utf-8");
console.log(calibrateDuplicates(content));

