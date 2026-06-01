# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            head = list1
            curr = list1
            pause = list2
        else:
            head = list2
            curr = list2
            pause = list1
        
        temp = None

        while True:

            if curr.next == None:
                curr.next = pause
                return head

            if curr.next.val <= pause.val:
                curr = curr.next
            else:
                temp = curr.next
                curr.next = pause
                curr = pause
                pause = temp
        
            



            

            
            
            
                

            





        