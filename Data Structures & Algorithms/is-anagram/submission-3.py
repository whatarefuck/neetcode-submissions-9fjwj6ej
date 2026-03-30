class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if not hashmap.get(i):
                hashmap[i] = 1
                continue
            hashmap[i] += 1
                

        for i in t:
            if not i in hashmap:
                return False
            hashmap[i] -= 1
            if hashmap[i] < 0:
                return False
        return not [value for value in hashmap.values() if value > 0]