from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        ret = begin = maxf = 0
        for end in range(len(s)):
            char = s[end]
            frequency[char] += 1
            maxf = max(maxf, frequency[char])

            while (end - begin + 1) - maxf > k:
                frequency[s[begin]] -= 1
                begin += 1

            ret = max(ret, end - begin + 1)

        return ret