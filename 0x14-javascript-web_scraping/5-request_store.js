#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, data, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
