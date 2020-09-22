#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const filename = process.argv[3];
const url = process.argv[2];
request(url).pipe(fs.createWriteStream(filename));
