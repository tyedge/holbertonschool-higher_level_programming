#!/usr/bin/node

let next = 0;
let arr = process.argv.slice(2);
if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.slice(2).length <= 1) {
  console.log(0);
} else {
  arr = arr.sort();
  next = arr[arr.length - 2];
  console.log(parseInt(next));
}
