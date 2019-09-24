#!/usr/bin/node

const request = require('request');
const fd = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) { console.log(error); }
  fd.writeFile(path, body, 'utf8', (error) => {
    if (error) { console.log(error); }
  });
});
