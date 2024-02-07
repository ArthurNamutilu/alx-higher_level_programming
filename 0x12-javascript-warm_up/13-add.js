#!/usr/bin/node

const add = (x, y) => {
  return x + y;
};
// exported as a property named 'add'
module.exports.add = add;
