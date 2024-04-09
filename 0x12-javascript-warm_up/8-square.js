#!/usr/bin/node
if (process.argv[2] === undefined ||
    Number.isNaN(Number(process.argv[2]))) {
  console .log('Missing size');
} else {
  const x = parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
