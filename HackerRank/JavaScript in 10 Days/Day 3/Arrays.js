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

/**
 *   Return the second largest number in the array.
 *   @param {Number[]} nums - An array of numbers.
 *   @return {Number} The second largest number in the array.
 **/
function getSecondLargest(nums) {
  // Complete the function
  let first_max = Number.NEGATIVE_INFINITY
  let second_max = Number.NEGATIVE_INFINITY

  for (const num of nums) {
    if (first_max < num) {
      second_max = first_max
      first_max = num
    } else if (second_max < num && num != first_max) {
      second_max = num
    }
  }
  return second_max
}