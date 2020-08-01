class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, carry = 0):
        value = l1.value + l2.value + carry
        carry = value // 10
        result = ListNode(value % 10)

        if (l2.next != None or l1.next != None or carry != 0):
            if l2.next == None:
                l2.next = ListNode(0)
            if l1.next == None:
                l1.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return result
        
# Test Cases
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = Solution().addTwoNumbers(l1, l2)

while result:
    print(result.value),
    result = result.next