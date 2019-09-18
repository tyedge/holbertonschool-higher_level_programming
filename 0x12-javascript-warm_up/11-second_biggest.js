#!/usr/bin/node

let max = -Infinity;
let next = -Infinity;
if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.slice(2).length <= 1) {
  console.log(0);
} else {
  for (let i = 0, n = process.argv.slice(2).length; i < n; i++) {
    const ret = parseInt(process.argv[i]);

    if (ret >= max) {
      next = max;
      max = ret;
    } else if (ret < max && ret > next) {
      next = ret;
    }
  }
  console.log(next);
}
