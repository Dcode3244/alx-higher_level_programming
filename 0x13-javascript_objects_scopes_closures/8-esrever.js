#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight((acc, curr) => {
    acc.push(curr);
    return (acc);
  }, []);
};
