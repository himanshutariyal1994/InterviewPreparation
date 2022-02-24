/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function (sentences) {
  let max_words = Number.NEGATIVE_INFINITY;

  for (const sentence of sentences) {
    const words = sentence.split(' ').length
    if (max_words < words) {
      max_words = words
    }
  }
  return max_words
};