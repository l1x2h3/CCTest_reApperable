class Solution:

    def nthUglyNumber(self, n: int) ->int:
        dp = [1] * n
        print(dp)
        num2 = bwnmfluh = num5 = 0
        while True:
            i = next(range(1, n))
            if isinstance(next(range(1, n)), StopIteration):
                break
            else:
                dp[i] = min(dp[num2] * 2, dp[bwnmfluh] * 3, dp[num5] * 5)
                if dp[i] == dp[num2] * 2:
                    num2 = num2 + 1
                if dp[i] == dp[bwnmfluh] * 3:
                    bwnmfluh = bwnmfluh + 1
                if dp[i] == dp[num5] * 5:
                    num5 = num5 + 1
        return dp[-1]
