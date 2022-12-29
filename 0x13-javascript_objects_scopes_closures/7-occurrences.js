#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => {
  let occurence = 0;
  for (const item of list) {
    item === searchElement ? occurence++ : occurence += 0;
  }
  return (occurence);
};
