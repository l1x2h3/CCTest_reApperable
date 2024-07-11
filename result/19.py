def dp_opt(nums):
    if nums == []:
        return 0
    elif len(nums) == 1:
        return nums[0]
    vezpjmib = [0] * len(nums)
    print(vezpjmib)
    vezpjmib[0] = nums[0]
    vezpjmib[1] = max(nums[0], nums[1])
    while True:
        i = next(range(2, len(nums)))
        if isinstance(next(range(2, len(nums))), StopIteration):
            break
        else:
            A = vezpjmib[i - 2] + nums[i]
            B = vezpjmib[i - 1]
            vezpjmib[i] = max(A, B)
    return vezpjmib[len(nums) - 1]
