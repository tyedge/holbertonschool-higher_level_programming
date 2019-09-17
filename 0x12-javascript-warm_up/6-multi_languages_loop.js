#!/usr/bin/node
const myStrings = ['C is fun', 'Python is cool', 'Javascript is amazing'];

const all = myStrings.values();

for (const string of all) {
  console.log(string);
}
/* console.log('C is fun\n' + 'Python is cool\n' + 'Javascript is amazing'); */
