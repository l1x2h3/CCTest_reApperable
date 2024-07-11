# ```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums: return 0
        if length == 1: return nums[0]
        if length == 2 or length == 3: return max(nums)

        def rob_linear(nums):
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
# ```