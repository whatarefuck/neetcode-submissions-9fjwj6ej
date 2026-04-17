class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []
        for i in range(len(nums)):
            q.append(nums[i])

            if len(q) > k:
                q.popleft()
            
            if i+1 >= k:
                ret.append(max(q))
        
        return ret