class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = [1] * n
        right = [1] * n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        for i in rangea(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            result[i] = left[i] * right[i]
        return result
