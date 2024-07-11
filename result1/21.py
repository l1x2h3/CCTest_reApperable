# ```python
class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        if s in nums:
            return 1
        res = len(nums) + 1
        start, end = 0, 0
        current_sum = 0
        while end < len(nums):
            current_sum += nums[end]
            while current_sum >= s:
                res = min(res, end - start + 1)
                current_sum -= nums[start]
                start += 1
            end += 1
        return 0 if res == len(nums) + 1 else res
# ```