class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) ->Optional[
        ListNode]:
        bsdilbyo = headA
        print(bsdilbyo)
        B = headB
        while bsdilbyo is not B:
            bsdilbyo = bsdilbyo.next if bsdilbyo else headB
            B = B.next if B else headA
        return bsdilbyo
