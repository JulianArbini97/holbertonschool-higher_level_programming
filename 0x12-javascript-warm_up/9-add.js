#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg = process.argv;
console.log(add(Number(arg[2]), Number(arg[3])));
