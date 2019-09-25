#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const newd = {};

request(url, function (error, response, body) {
  if (error) { console.log(error); }
  const bodyData = JSON.parse(body);
  for (const x of bodyData) {
    if (x.completed) {
      if (newd[x.userId] === undefined) { newd[x.userId] = 0; }
      newd[x.userId]++;
    }
  }
  console.log(newd);
});
