class Solution:
    def rob(self, nums: List[int]) -> int:
        # 首尾相邻
        length = len(nums)
        if not nums: return 0
        if length == 1:
            return nums[0]
        elif length == 2 or length == 3:
            return max(nums)
        a = nums[1:]  # 1-n
        b = nums[:length - 1]

        def fun(nums):
            length = len(nums)
            dp = [0] * length
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, length):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[length - 1]

        return max(fun(a), fun(b))
