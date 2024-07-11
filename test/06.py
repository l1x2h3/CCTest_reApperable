# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.fromNodeToNum(l1)
        num2 = self.fromNodeToNum(l2)
        list = self.fromNumToLinkList(num1 + num2)
        return list

    def fromNodeToNum(self, linkList):
        num = 0
        digit = 0
        while linkList is not None:
            num = num + linkList.val * (10 ** digit)
            digit = digit + 1
            linkList = linkList.next
        return num

    def fromNumToLinkList(self, num):
        linkList = ListNode()
        if num >= 10:
            linkList.val = num % 10
            num = num // 10
            linkList.next = self.fromNumToLinkList(num)
        else:
            linkList.val = num
            linkList.next = None
        return linkList


# 作者：seanlee
# 链接：https://leetcode.cn/problems/add-two-numbers/solutions/2811517/jian-ji-bao-li-by-infallible-chatelethm4-fcs1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。