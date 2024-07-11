# ```python
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        total_len = len(nums1)
        if total_len % 2 == 0:
            return (nums1[total_len // 2] + nums1[total_len // 2 - 1]) / 2
        else:
            return nums1[total_len // 2]
# ```