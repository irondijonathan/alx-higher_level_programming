#!/usr/bin/node

// This Converts a number from base 10 to another base passed as argument/input


exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
