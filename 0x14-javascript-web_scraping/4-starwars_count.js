#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let appearences = 0;

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const iterable = JSON.parse(body).results;
  const listlen = iterable.length;
  let cont = 0;
  let cont2 = 0;
  for (cont = 0; cont < listlen; cont++) {
    for (cont2 = 0; cont2 < iterable[cont].characters.length; cont2++) {
      if (iterable[cont].characters[cont2].includes('/18/')) {
        appearences += 1;
      }
    }
  }
  console.log(appearences);
});
