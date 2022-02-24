/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  const len = digits.length - 1
  if (digits[len] < 9) {
    digits[len]++
    return digits
  }

  for (let i = len; i >= 0; i--) {
    digits[i]++;

    if (digits[i] > 9) {
      digits[i] = 0;
    } else {
      return digits
    }
  }

  digits.unshift(1);
  return digits;
};