#!/usr/bin/node

const num = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let text = '';
    for (let j = 0; j < num; j++) {
      text += 'X' + '';
    }
    console.log(text);
  }
}
