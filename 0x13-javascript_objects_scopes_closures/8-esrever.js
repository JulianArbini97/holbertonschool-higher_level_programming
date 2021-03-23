#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let counter;
  const length = list.length - 1;

  for (counter = length; counter >= 0; counter--) {
    reversed.push(list[counter]);
  }
  return (reversed);
};
