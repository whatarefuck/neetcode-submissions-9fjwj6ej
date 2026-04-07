class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x.lower() for x in s if x.isalnum()])
        for i in range(len(s)):
            if s[i-1] != s[-i]:
                return False
        return True