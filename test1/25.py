# ```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        num2 = num3 = num5 = 0
        for i in range(1, n):
            dp[i] = min(dp[num2] * 2, dp[num3] * 3, dp[num5] * 5)
            if dp[i] == dp[num2] * 2:
                num2 += 1
            if dp[i] == dp[num3] * 3:
                num3 += 1
            if dp[i] == dp[num5] * 5:
                num5 += 1
        return dp[-1]
# ```