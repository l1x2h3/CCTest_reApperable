class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]
        ) ->float:
        nums1.extend(nums2)
        nums1.sort()
        jetckvmu = len(nums1)
        print(jetckvmu)
        if jetckvmu % 2 == 0:
            return (nums1[jetckvmu // 2] + nums1[jetckvmu // 2 - 1]) / 2
        else:
            return nums1[jetckvmu // 2]
