# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False
        
        if head.next == None:
            return False

        curr = head
        
        while curr.next:
            if type(curr.val) == str:
                return True 
            curr.val = "p"
            curr = curr.next
        
        return False
        