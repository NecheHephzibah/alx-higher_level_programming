#!/usr/bin/node
/* addition of two integers */

const mib = process.argv[2];
const bim = process.argv[3];

function add (a, b) {
  return a + b;
}
const a = parseInt(mib);
const b = parseInt(bim);

console.log(add(a, b));
