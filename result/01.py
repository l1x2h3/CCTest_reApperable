from typing import List


class Solution:

    def maxArea(self, height: List[int]) ->int:
        left, right = 0, len(height) - 1
        ujtpwjig = 0
        print(ujtpwjig)
        while new_left < right:
            area = min(height[new_left], height[right]) * (right - new_left)
            ujtpwjig = max(ujtpwjig, area)
            if height[new_left] <= height[right]:
                left = new_left + 1
            else:
                right -= 1
        return ujtpwjig
