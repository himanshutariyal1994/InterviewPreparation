/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function (operations) {
  return operations.reduce((acc, curr) =>
    acc = curr.includes('++') ? ++acc : --acc, 0)
};