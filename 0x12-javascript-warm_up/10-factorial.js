#!/usr/bin/node

function fact (num) {
  if (num <= 1 || !num) {
    return (1);
  }
  return (num * fact(num - 1));
}

const result = fact(process.argv[2]);
console.log(result);
