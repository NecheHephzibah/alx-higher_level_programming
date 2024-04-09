#!/usr/bin/node
if (process.argv[2] === undefined ||
    Number.isNaN(Number(process.argv[2]))) {
  console .log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
