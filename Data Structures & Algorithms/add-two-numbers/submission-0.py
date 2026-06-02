# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = l1
        count = 0
        num1 = 0

        while True:
            num1 = num1 + curr.val * (10**count)
            count = count + 1
            if curr.next == None:
                break
            curr = curr.next

        curr = l2
        count = 0
        num2 = 0

        while True:
            num2 = num2 + curr.val * (10**count)
            count = count + 1
            if curr.next == None:
                break
            curr = curr.next

        num = num1 + num2
        numstr = str(num)
        nodig = len(numstr)

        head = ListNode(num-(num//10)*10)
        count = 1

        if nodig == 1:
            return head

        curr = head

        while True:
            curr.next = ListNode((num//(10**count))-((num//(10**(count+1)))*10))
            count = count + 1
            if count == nodig:
                return head
            curr = curr.next


        






        