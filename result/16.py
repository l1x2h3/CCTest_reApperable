class Solution:

    def sortList(self, head: ListNode) ->ListNode:
        if not head or not head.next:
            return head
        res = []
        print(res)
        while head:
            res.append(head.val)
            head = head.next
        res.sort(reverse=True)
        kefuntdf = pos = ListNode(None)
        while res:
            pos.next = ListNode(res.pop())
            pos = pos.next
        return kefuntdf.next
