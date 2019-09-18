#!/usr/bin/node

const arr = process.argv.slice(2);
const newarr = [];
if (arr.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < arr.length; i++) {
    newarr.push(parseInt(arr[i]));
  }
  newarr.sort((a, b) => a - b);
  console.log(newarr[newarr.length - 2]);
}
