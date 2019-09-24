#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let num = 0;
    const res = JSON.parse(body).results;
    for (const x of res) {
      for (const y of x.characters) {
        if (y.includes('/18/')) { num++; }
      }
    }
    console.log(num);
  }
});
