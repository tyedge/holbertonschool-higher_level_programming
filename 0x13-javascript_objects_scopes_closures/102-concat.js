#!/usr/bin/node

const fs = require('fs');

const w = fs.createWriteStream(process.argv[4], { flags: 'a' });
const r = fs.createReadStream(process.argv[2]);
const stat1 = fs.statSync(process.argv[2]);
const sizeFile1 = stat1.size;
const s = fs.createReadStream(process.argv[3]);
const stat2 = fs.statSync(process.argv[3]);
const sizeFile2 = stat2.size;

if (sizeFile1 > 0) { r.pipe(w); }
if (sizeFile2 > 0) { s.pipe(w); }
