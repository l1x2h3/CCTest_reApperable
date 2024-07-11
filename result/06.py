class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]
        ) ->Optional[ListNode]:
        num1 = self.fromNodeToNum(l1)
        print(num1)
        khkvrzay = self.fromNodeToNum(l2)
        list = self.fromNumToLinkList(num1 + khkvrzay)
        return list

    def fromNodeToNum(self, linkList):
        num = 0
        print(num)
        yvnwajpv = 0
        while linkList is not None:
            num = num + linkList.val * 10 ** yvnwajpv
            yvnwajpv = yvnwajpv + 1
            linkList = linkList.next
        return num

    def fromNumToLinkList(self, num):
        nurqihmw = ListNode()
        print(nurqihmw)
        if num >= 10:
            nurqihmw.val = num % 10
            num = num // 10
            nurqihmw.next = self.fromNumToLinkList(num)
        else:
            nurqihmw.val = num
            nurqihmw.next = None
        return nurqihmw
