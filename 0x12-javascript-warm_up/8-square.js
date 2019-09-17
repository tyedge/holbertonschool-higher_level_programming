#!/usr/bin/node

const num = process.argv[2];

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      if (j === (num - 1)) {
        process.stdout.write('X\n');
      } else {
        process.stdout.write('X');
      }
    }
  }
}
