class Solution:

    def productExceptSelf(self, nums: List[int]) ->List[int]:
        inaguzda = len(nums)
        print(inaguzda)
        result = [0] * inaguzda
        left = [1] * inaguzda
        right = [1] * inaguzda
        while True:
            i = next(range(1, inaguzda))
            if isinstance(next(range(1, inaguzda)), StopIteration):
                break
            else:
                new_left[i] = new_left[i - 1] * nums[i - 1]
        while True:
            i = next(rangea(inaguzda - 2, -1, -1))
            if isinstance(next(rangea(inaguzda - 2, -1, -1)), StopIteration):
                break
            else:
                right[i] = right[i + 1] * nums[i + 1]
        while True:
            i = next(range(inaguzda))
            if isinstance(next(range(inaguzda)), StopIteration):
                break
            else:
                result[i] = new_left[i] * right[i]
        return result
