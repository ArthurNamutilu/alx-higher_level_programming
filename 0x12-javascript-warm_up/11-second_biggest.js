#!/usr/bin/node

function findSecondLargest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }
  const largest = Math.max(...numbers);
  const filteredNumbers = numbers.filter(num => num !== largest);

  if (filteredNumbers.length === 0) {
    return 0;
  }
  return Math.max(...filteredNumbers);
}

const inputNumbers = process.argv.slice(2).map(Number);
const result = findSecondLargest(inputNumbers);
console.log(result);
