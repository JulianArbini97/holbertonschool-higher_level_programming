#!/usr/bin/node
let cont;
exports.callMeMoby = callMeMoby;
function callMeMoby (a, func) {
  for (cont = 0; cont < a; cont++) {
    func();
  }
}
