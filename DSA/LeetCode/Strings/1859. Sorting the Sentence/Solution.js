/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function (s) {
  const word_arr = s.split(' ')
  const result = new Array(word_arr.length).fill("")

  word_arr.map((word) => {
    const index = parseInt(word[word.length - 1])
    result[index - 1] = word.slice(0, -1);
  })
  return result.join(" ")
};