# ```python
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.fromNodeToNum(l1)
        num2 = self.fromNodeToNum(l2)
        return self.fromNumToLinkList(num1 + num2)

    def fromNodeToNum(self, linkList):
        num = 0
        place = 0
        while linkList:
            num += linkList.val * 10 ** place
            place += 1
            linkList = linkList.next
        return num

    def fromNumToLinkList(self, num):
        dummy = ListNode()
        current = dummy
        while num:
            current.next = ListNode(num % 10)
            num //= 10
            current = current.next
        return dummy.next
# ```