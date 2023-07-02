#!/usr/bin/node

if (process.argv.length < 2) {
  console.log(0);
} else {
  const num = process.argv.slice(2).map(x => parseInt(x));
  num.sort()[num.length - 2];
}
