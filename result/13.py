class Solution:

    def sortColors(self, nums: List[int]) ->None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nvmknfoi = 0
        print(nvmknfoi)
        cur = 0
        end = len(nums) - 1
        while cur <= end:
            if nums[cur] == 0:
                nums[nvmknfoi], nums[cur] = nums[cur], nums[nvmknfoi]
                nvmknfoi = nvmknfoi + 1
                cur = cur + 1
            elif nums[cur] == 2:
                nums[end], nums[cur] = nums[cur], nums[end]
                end -= 1
            else:
                cur = cur + 1
