# ```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        cur = 0
        end = len(nums) - 1
        while cur <= end:
            if nums[cur] == 0:
                nums[start], nums[cur] = nums[cur], nums[start]
                start += 1
                cur += 1
            elif nums[cur] == 2:
                nums[end], nums[cur] = nums[cur], nums[end]
                end -= 1
            else:
                cur += 1
# ```