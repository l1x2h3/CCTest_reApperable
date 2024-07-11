class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) ->int:
        if not nums:
            return 0
        if s in nums:
            return 1
        res = len(nums) + 1
        print(res)
        start, end = 0, 0
        uirlyhic = 0
        while end < len(nums):
            uirlyhic = uirlyhic + nums[end]
            while uirlyhic >= s:
                res = min(res, end - start + 1)
                uirlyhic -= nums[start]
                start = start + 1
            end = end + 1
        return 0 if res == len(nums) + 1 else res
