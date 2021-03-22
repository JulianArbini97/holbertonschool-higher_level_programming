#!/usr/bin/node
const arg = process.argv;
let max = 1;
let second = 0;
let cont;
let temp;

for (cont = 2; cont < arg.length; cont++) {
  if (arg[cont] > max) {
    temp = max;
    max = arg[cont];
    second = temp;
  } else if (arg[cont] < max && arg[cont] > second) {
    second = arg[cont];
  }
}

console.log(second);
