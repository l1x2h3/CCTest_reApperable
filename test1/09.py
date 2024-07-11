# ```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result = 0
        while start < end:
            res = min(height[start], height[end]) * (end - start)
            result = max(result, res)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return result
# ```