# ```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for x in range(i + 1, len(self.prefix_sum)):
            self.prefix_sum[x] += diff

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j + 1] - self.prefix_sum[i]
# ```