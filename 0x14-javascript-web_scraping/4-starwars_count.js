#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const purl = 'https://swapi-api.hbtn.io/api/people/18/';

request.get(url, function (err, res, body) {
  const films = JSON.parse(body).results;
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes(purl)) {
        count++;
      }
    }
    console.log(count);
  }
});
