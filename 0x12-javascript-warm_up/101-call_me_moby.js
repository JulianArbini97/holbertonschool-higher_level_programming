#!/usr/bin/node
let cont;
exports.callMeMoby = callMeMoby;
function callMeMoby (x, func) {
  for (cont = 0; cont < x; cont++) {
    func();
  }
}
