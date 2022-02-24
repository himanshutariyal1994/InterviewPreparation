/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function (accounts) {
  let max_wealth = Number.NEGATIVE_INFINITY

  for (let i = 0; i < accounts.length; i++) {
    const sum = accounts[i].reduce((acc, curr) => acc + curr, 0);

    if (max_wealth < sum) {
      max_wealth = sum
    }
  }
  return max_wealth
};