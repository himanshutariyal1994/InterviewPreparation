/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function (s) {
  let counter = 0;
  let temp = 0;

  for (const letter of s) {
    (letter === "L") ? ++temp: --temp;

    if (temp === 0) ++counter
  }
  return counter;
};