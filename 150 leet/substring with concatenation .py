class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return[]

        word_length = len(words[0])
        total_words = len(words)
        total_length = word_length * total_words
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result_indices = []

        for i in range(len(s) - total_length + 1):
            seen_words = {}
            j = 0

            while j < total_words:
                word_index = i + j * word_length
                word = s[word_index:word_index + word_length]
                if word in word_count:
                    if word in seen_words:
                        seen_words[word] += 1
                    else:
                        seen_words[word] = 1
                    if seen_words[word] > word_count[word]:
                        break
                else:
                    break
                j += 1
            if j == total_words:
                result_indices.append(i)
        return result_indices
