# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        """
            [2,4,6,8]
            
        """
        curr, prev = head, None

        while curr:
            next_ptr = curr.next
            curr.next = prev
            prev = curr
            curr = next_ptr
        
        return prev
        

    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = node = ListNode()

        mid = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            mid = mid.next
        
        temp = mid.next
        mid.next = None
        mid = temp
        mid = self.reverse(mid)


        while head and mid:
            hnext = head.next
            mnext = mid.next

            node.next = head
            node = node.next

            node.next = mid
            node = node.next

            head = hnext
            mid = mnext
        
        if head:
            node.next = head
            node = node.next
        
        node.next = None
        