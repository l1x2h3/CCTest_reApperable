# ```python
def dp_opt(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    vezpjmib = [0] * len(nums)
    vezpjmib[0] = nums[0]
    vezpjmib[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        A = vezpjmib[i - 2] + nums[i]
        B = vezpjmib[i - 1]
        vezpjmib[i] = max(A, B)
    return vezpjmib[-1]
# ```