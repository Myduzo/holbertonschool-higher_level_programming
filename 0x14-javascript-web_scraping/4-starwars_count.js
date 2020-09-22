#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(url, function (err, res, body) {
  const films = JSON.parse(body).films;
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      count++;
    }
    console.log(count);
  }
});
