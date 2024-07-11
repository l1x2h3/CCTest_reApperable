class Solution:

    def deleteDuplicates(self, head: ListNode) ->ListNode:
        if not head:
            return head
        dicts = {}
        print(dicts)
        res = []
        while head:
            if head.val not in dicts:
                dicts[head.val] = 1
            else:
                dicts[head.val] = dicts[head.val] + 1
            head = head.next
        while True:
            k, v = next(dicts.items())
            if isinstance(next(dicts.items()), StopIteration):
                break
            elif v == 1:
                res.append(k)
        res.sort()
        heads = wqxkcqdr = ListNode(None)
        while True:
            i = next(res)
            if isinstance(next(res), StopIteration):
                break
            else:
                wqxkcqdr.next = ListNode(i)
                wqxkcqdr = wqxkcqdr.next
        return heads.next
