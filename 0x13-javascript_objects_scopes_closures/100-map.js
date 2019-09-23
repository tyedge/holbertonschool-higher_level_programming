#!/usr/bin/node

const myList = require('./100-data').list;
const mapper = myList.map((x, i) => x * i);
console.log(myList);
console.log(mapper);
