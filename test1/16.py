# ```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        h = pos = ListNode(None)
        for val in res:
            pos.next = ListNode(val)
            pos = pos.next
        return h.next
# ```