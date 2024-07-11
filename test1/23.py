# ```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        right = 1
        for i in range(n):
            result[i] *= left
            left *= nums[i]
            result[n - 1 - i] *= right
            right *= nums[n - 1 - i]
        return result
# ```