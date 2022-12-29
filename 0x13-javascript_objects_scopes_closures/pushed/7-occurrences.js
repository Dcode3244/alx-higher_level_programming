#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  function counter (acc, curr) {
    return (curr === searchElement ? acc += 1 : acc);
  }
  return (list.reduce(counter, 0));
};
