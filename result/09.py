class Solution:

    def maxArea(self, height: List[int]) ->int:
        start = 0
        print(start)
        end = len(height) - 1
        zvjzxrec = 0
        while start < end:
            res = min(height[start], height[end]) * (end - start)
            zvjzxrec = max(zvjzxrec, res)
            if height[start] >= height[end]:
                end -= 1
            else:
                start = start + 1
        return zvjzxrec
