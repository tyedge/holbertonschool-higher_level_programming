#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) { console.log(error); }
  const res = JSON.parse(body).characters;
  for (const x of res) {
    request(x, function (error, response, body) {
      if (error) { console.log(error); }
      console.log(JSON.parse(body).name);
    });
  }
});
