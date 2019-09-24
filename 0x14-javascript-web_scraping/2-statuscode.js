#!/usr/bin/node

const request = require('request');
const file = process.argv[2];

request(file, function (error, response) {
  if (error) { console.log(error); }
  console.log('code:', response.statusCode);
});
