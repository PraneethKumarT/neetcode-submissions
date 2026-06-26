# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge2Lists(l1, l2))

            lists = mergedLists

        return lists[0]


    def merge2Lists(self, l1, l2):

        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        
        return temp.next


"""
[] [] [] [] [] 
  [].   [].  []
    [1,3,5]. [1, 2, 6]
       []


[] [] [] [] [] []

"""