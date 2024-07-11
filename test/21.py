class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:return 0
        if s in nums:return 1

        res = len(nums) + 1
        start,end = 0,0
        t = 0
        while end < len(nums):
            t += nums[end]
            while t >= s:
                res = min(res,end-start+1)
                t -= nums[start]
                start += 1
            end += 1
        return 0 if res == len(nums) + 1 else res

