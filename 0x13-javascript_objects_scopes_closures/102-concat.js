#!/usr/bin/node

var fs = require('fs');

var w = fs.createWriteStream(process.argv[4], { flags: 'a' });
var r = fs.createReadStream(process.argv[2]);
var s = fs.createReadStream(process.argv[3]);

r.pipe(w);
s.pipe(w);
