class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
        
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                ret[stackInd] = i - stackInd
            stack.append((t, i))
        return ret