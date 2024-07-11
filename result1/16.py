# ```python
class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        dummy = pos = ListNode(None)
        for val in res:
            pos.next = ListNode(val)
            pos = pos.next
        return dummy.next
# ```