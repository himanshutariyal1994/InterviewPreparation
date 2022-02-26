'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function () {
  inputString = inputString.split('\n');

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function printTableOfN(n) {
  for (let i = 1; i < 11; i++) {
    console.log(`${n} x ${i} = ${n*i}`)
  }
}

function main() {
  const n = parseInt(readLine().trim(), 10);
  printTableOfN(n)
}