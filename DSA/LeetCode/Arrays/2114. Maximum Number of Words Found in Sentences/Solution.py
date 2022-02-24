class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most_words = float('-inf')

        for s in sentences:
            count = len(s.split(' '))

            if count > most_words:
                most_words = count

        return most_words
