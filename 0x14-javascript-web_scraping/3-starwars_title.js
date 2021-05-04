#!/usr/bin/node

const request = require('request');
const page_url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(page_url, (err, data, body) => {
  if (err) {
    console.log(err);
    return
  }
  console.log(JSON.parse(body).title);
});
