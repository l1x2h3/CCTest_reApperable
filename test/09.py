class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result = 0
        while start < end:
            res = min(height[start],height[end]) * (end - start)
            result = max(result,res)
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return result
