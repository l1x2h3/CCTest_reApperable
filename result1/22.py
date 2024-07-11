# ```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
        
        def helper(nums):
            n = len(nums)
            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
        
        return max(helper(nums[:-1]), helper(nums[1:]))
# ```