from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words

        word_count = Counter(words)
        ans = []

        # Try every possible starting offset
        for offset in range(word_len):
            left = offset
            curr_count = {}
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1

                    # Shrink window if a word appears too many times
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    # Found a valid window
                    if count == total_words:
                        ans.append(left)

                        # Move window forward
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # Invalid word: reset window
                    curr_count.clear()
                    count = 0
                    left = right + word_len

        return ans