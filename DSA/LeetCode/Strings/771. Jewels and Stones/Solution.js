/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  const stone_set = new Set(jewels);

  return stones.split('').reduce((acc, curr) => stone_set.has(curr) ? ++acc : acc, 0);
};