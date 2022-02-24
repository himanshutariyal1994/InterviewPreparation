'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
  inputString += inputStdin;
});

process.stdin.on('end', _ => {
  inputString = inputString.trim().split('\n').map(string => {
    return string.trim();
  });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function getLetter(s) {
  const char = s[0].toLowerCase();
  let letter;

  switch (true) {
    case 'aeiou'.includes(char):
      letter = 'A'
      break;
    case 'bcdfg'.includes(char):
      letter = 'B'
      break;
    case 'hjklm'.includes(char):
      letter = 'C'
      break;
    case 'npqrstvwxyz'.includes(char):
      letter = 'D'
      break;
    default:
      letter = char
  }
  return letter;
}