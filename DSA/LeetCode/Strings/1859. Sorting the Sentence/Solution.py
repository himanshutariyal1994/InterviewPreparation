class Solution:
    def sortSentence(self, s: str) -> str:
        word_arr = s.split(' ')
        result_arr = [""] * len(word_arr)

        for i in range(len(word_arr)):
            word = word_arr[i]
            index = int(word[len(word)-1])
            result_arr[index-1] = word[:-1]

        return " ".join(result_arr)
