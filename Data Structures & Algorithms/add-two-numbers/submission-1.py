# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        dummy = head


        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sumVal = val1 + val2 + carry
            carry = sumVal//10
            sumVal = sumVal%10

            head.next = ListNode(sumVal)
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

        """
case 1: same no of digits
231
124

case 2: diff
232
12

consider:
carry
"""

        