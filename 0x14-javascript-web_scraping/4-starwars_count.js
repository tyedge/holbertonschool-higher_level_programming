#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {

  } else {
    let num = 0;
    const res = JSON.parse(body).results;
    let x, y;
    for (x of res) {
      for (y of x.characters) {
        if (y === 'https://swapi.co/api/people/18/') { num++; }
      }
    }
    console.log(num);
  }
});
