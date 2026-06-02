# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None:
            return None
        elif head.next == None:
            return None

        curr = head
        count = 1

        while curr.next:
            curr = curr.next
            count = count + 1

        curr = head
        leng = count
        count = 1

        if 1 == leng-n:
            head.next = head.next.next
            return head
        elif 0 == leng-n:
            return head.next

        while curr.next:
            curr = curr.next
            count = count + 1
            if count == leng - n:
                curr.next = curr.next.next
                return head

        

        