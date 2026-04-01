from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums)+1)]
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        
        for num, count in counts.items():
            frequency[count].append(num)
        
        ret = []
        for i in range(len(frequency) -1, 0, -1):
                for num in frequency[i]:
                    ret.append(num)
                    if len(ret) == k:
                        return ret