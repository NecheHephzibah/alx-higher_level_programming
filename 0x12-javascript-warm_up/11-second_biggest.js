#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const n = process.argv.slice(2).map(Number);
  const n2 = n.sort(function (a, b) { return b - a; })[1];
  console.log(n2);
}
