#!/usr/bin/node

let arr = process.argv;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  arr = arr.sort();
  let next = arr[arr.length - 2];
  console.log(parseInt(next));
}
