#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let myVar = 0;
  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      myVar += 1;
    }
  }
  return myVar;
};
