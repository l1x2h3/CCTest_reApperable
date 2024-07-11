# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 双指针从头来过
        # “如果走到尽头也没有找到你都踪影，那么我就换另一条路从头寻找”
        # “我也一样。”
        A = headA
        B = headB
        while A is not B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

# 作者：karma.
# 链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/2732694/ru-guo-zou-dao-jin-tou-ye-mei-you-zhao-d-1fn7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。