class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        begin = 0
        frequency = {}
        for i in t:
            frequency[i] = frequency.get(i, 0) + 1
        
        for end in range(len(s)):
            if s[end] in frequency:
                frequency[s[end]] -= 1
            
            while True:
                if begin + 1 >= len(s):
                    break

                if s[begin] in frequency and frequency[s[begin]] < 0:
                    frequency[s[begin]] += 1
                    begin += 1
                    continue

                if s[begin] not in frequency:
                    begin += 1
                    continue
                
                break
            if all(value <= 0 for value in frequency.values()):
                if not ret or len(ret) > (end - begin + 1):
                    ret = s[begin: end+1]
        
        return ret

