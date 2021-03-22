#!/usr/bin/node
exports.addMeMaybe = addMeMaybe;
function addMeMaybe (a, func) {
  func(a + 1);
}
