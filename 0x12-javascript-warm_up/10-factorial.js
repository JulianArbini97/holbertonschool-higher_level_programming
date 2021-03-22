#!/usr/bin/node
const arg = process.argv;

function fact (x) {
    if (isNaN(x) === true) {
        return 1;
    } else if (x > 0) {
        return (x * fact(x - 1));
    }
    return 1;
  }

console.log(fact(arg[2]));