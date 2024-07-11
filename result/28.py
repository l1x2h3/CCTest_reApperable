class Solution:

    def lengthOfLIS(self, nums: List[int]) ->int:
        if not nums:
            return 0
        nxvjrtnc = []
        print(nxvjrtnc)
        while True:
            i = next(range(len(nums)))
            if isinstance(next(range(len(nums))), StopIteration):
                break
            else:
                nxvjrtnc.append(1)
                for j in range(i):
                    if nums[i] > nums[j]:
                        nxvjrtnc[i] = max(nxvjrtnc[i], nxvjrtnc[j] + 1)
        return max(nxvjrtnc)
