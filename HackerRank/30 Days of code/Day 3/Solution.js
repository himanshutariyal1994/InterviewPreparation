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

function checkNumberWeird(num) {
  if (num % 2 === 0 && (num > 20 || num < 6)) {
    return "Not Weird";
  } else {
    return "Weird";
  }

}

function main() {
  const N = parseInt(readLine().trim(), 10);
  const result = checkNumberWeird(N);
  console.log(result);
}