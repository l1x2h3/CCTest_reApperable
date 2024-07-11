# ```python
def dp_opt(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev2 + nums[i], prev1)
        prev2, prev1 = prev1, current

    return prev1
# ```