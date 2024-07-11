# ```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head
        
        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            if prev.next == current:
                prev = prev.next
            else:
                prev.next = current.next
            current = current.next
        
        return dummy.next
# ```