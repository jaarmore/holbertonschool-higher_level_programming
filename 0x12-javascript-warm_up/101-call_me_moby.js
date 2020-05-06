#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let cont = 1;
  while (cont <= x) {
    theFunction();
    cont++;
  }
};
