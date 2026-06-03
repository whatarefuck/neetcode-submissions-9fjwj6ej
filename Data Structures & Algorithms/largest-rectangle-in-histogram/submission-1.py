class Solution:
    def split_by_zero(self, heights: List[int]) -> List[List[int]]:
        lists = []
        sublist = []
        for i in heights:
            if i == 0:
                if sublist:
                    lists.append(sublist)
                sublist = []
                continue
            sublist.append(i)
        if sublist:
            lists.append(sublist)
        return lists if lists else [heights]

    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        lists = self.split_by_zero(heights)

        for sublist in lists:
            unique_heights = set(sublist)

            for level in unique_heights:
                current = []
                for height in sublist:
                    if height >= level:
                        current.append(height)
                        rectangle = level * len(current)
                        result = max(result, rectangle)
                    else:
                        current = []

        return result