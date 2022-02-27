/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function (s, indices) {
  const result = new Array(indices.length)
  for (const i in indices) {
    result[indices[i]] = s[i]
  }
  return result.join("")
};