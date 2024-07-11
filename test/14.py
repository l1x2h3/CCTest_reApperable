# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head

        dicts = {} # 记录出现的次数
        res = [] # 出现一次的数组
        while head:
            if head.val not in dicts:
                dicts[head.val] = 1
            else:
                dicts[head.val] += 1
            head = head.next
        for k,v in dicts.items():
            if v == 1:
                res.append(k)
        res.sort() # 排序
        heads = pos = ListNode(None)
        for i in res:
            pos.next = ListNode(i)
            pos = pos.next
        return heads.next
