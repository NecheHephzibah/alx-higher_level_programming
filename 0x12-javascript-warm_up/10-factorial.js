#!/usr/bin/node
/* a script that calulates and prints a factorial */
let argument = parseInt(process.argv[2]);
if (isNaN(argument)) {
  argument = 1;
}

function factorial (n) {
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(argument));
