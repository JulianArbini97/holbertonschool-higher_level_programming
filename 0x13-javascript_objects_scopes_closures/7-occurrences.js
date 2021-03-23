#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  let counter;

  for (counter = 0; counter < list.length; counter++) {
    if (list[counter] === searchElement) {
      occurrences++;
    }
  }
  return (occurrences);
};
