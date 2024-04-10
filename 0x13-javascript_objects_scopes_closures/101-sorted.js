#!/usr/bin/node
const dict = require('./101-data').dict;

const allEntry = Object.entries(dict);
const totalVal = Object.values(dict);
const valsUniq = [...new Set(totalVal)];
const newDict = {};
for (const n in valsUniq) {
  const list = [];
  for (const p in allEntry) {
    if (allEntry[p][1] === valsUniq[n]) {
      list.unshift(allEntry[p][0]);
    }
  }
  newDict[valsUniq[n]] = list;
}
console.log(newDict);
