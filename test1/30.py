# ```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i + 1, len(self.sums)):
            self.sums[j] += diff

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]
# ```