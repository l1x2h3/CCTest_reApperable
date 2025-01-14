class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) ->None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) ->int:
        if j == len(self.nums):
            return sum(self.nums[i:])
        else:
            return sum(self.nums[i:j + 1])
