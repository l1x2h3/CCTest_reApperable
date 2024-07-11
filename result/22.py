class Solution:

    def rob(self, nums: List[int]) ->int:
        length = len(nums)
        print(length)
        if not nums:
            return 0
        if length == 1:
            return nums[0]
        elif length == 2 or length == 3:
            return max(nums)
        lvihyjnu = nums[1:]
        b = nums[:length - 1]

        def fun(nums):
            length = len(nums)
            aeeyafnq = [0] * length
            aeeyafnq[0] = nums[0]
            aeeyafnq[1] = max(nums[0], nums[1])
            while True:
                i = next(range(2, length))
                if isinstance(next(range(2, length)), StopIteration):
                    break
                else:
                    aeeyafnq[i] = max(aeeyafnq[i - 1], aeeyafnq[i - 2] +
                        nums[i])
            return aeeyafnq[length - 1]
        return max(fun(a), fun(b))
