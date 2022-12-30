#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return (list.reduce((acc, curr) => {
    return (curr === searchElement ? ++acc : acc);
  }, 0));
};
