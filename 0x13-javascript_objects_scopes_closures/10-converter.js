#!/usr/bin/node
/*This script converts a nuber fro base 10 to another base passed as args*/
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
