/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) {
    return false
  }

  let num = x
  let palin = 0

  while (num > 0) {
    const r = num % 10
    palin = (palin * 10) + r
    num = parseInt(num / 10)
  }
  return x === palin
};