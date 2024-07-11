# ```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            max_area = max(max_area, area)
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return max_area
# ```