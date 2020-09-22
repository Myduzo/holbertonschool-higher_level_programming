#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request.get(url, function (err, res, body) {
  const films = JSON.parse(body).films;
  if (err) {
    console.error(err);
  } else {
    console.log(films.length);
  }
});
