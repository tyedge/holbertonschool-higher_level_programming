#!/usr/bin/node

const fs = require('fs');

const w = fs.createWriteStream(process.argv[4], { flags: 'a' });
const r = fs.createReadStream(process.argv[2]);
const s = fs.createReadStream(process.argv[3]);

r.pipe(w);
s.pipe(w);
