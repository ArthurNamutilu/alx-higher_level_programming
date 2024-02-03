#!/usr/bin/node

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else {
    let result = 1;
    for (let i = 1; i <= a; i++) {
      result *= i;
    }
    return result;
  }
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));
