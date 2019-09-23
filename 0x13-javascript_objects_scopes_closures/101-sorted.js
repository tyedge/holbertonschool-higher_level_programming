#!/usr/bin/node

const myDict = require('./101-data.js').dict;
const newd = {};
for (const val in myDict) {
  if (newd[myDict[val]] === undefined) {
    newd[myDict[val]] = [];
  }
  newd[myDict[val]].push(val);
}
console.log(newd);
