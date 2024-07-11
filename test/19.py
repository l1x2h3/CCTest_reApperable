def dp_opt(nums):
    if nums == []:
        return 0
    elif len(nums) == 1:
        return nums[0]

    opt = [0] * len(nums)  # 创建数组来存储

    opt[0] = nums[0]
    opt[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        A = opt[i - 2] + nums[i]
        B = opt[i - 1]
        opt[i] = max(A, B)

    return opt[len(nums) - 1]
