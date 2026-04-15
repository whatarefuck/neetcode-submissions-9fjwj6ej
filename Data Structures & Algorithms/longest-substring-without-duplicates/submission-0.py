class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        begin = 0
        ret = 0
        
        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[begin])
                begin += 1
            charSet.add(s[end])
            ret = max(ret, end - begin + 1)
        return ret
