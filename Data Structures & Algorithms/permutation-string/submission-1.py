class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        begin = 0
        end = len(s1) - 1
        frequency_s1 = {}
        frequency_window = {}

        for char in s1:
            frequency_s1[char] = frequency_s1.get(char, 0) + 1
        
        for end in range(len(s2)):
            frequency_window[s2[end]] = frequency_window.get(s2[end], 0) + 1
            if frequency_s1 == frequency_window:
                return True
            if end - begin + 1 >= len(s1):
                frequency_window[s2[begin]] -= 1
                if frequency_window[s2[begin]] == 0:
                    del frequency_window[s2[begin]]
                begin += 1
        
        return False