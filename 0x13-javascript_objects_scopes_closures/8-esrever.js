#!/usr/bin/node

exports.esrever = function (list) {
  const myArr = [];
  for (let a = 0; a < list.length; a++) {
    myArr.unshift(list[a]);
  }
  return myArr;
};
