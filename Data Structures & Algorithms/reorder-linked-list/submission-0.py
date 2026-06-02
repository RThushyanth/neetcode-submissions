# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None

        elif head.next == None:
            return None

        curr = head
        count = 1

        while curr.next:
            curr = curr.next
            count = count+1

        if count == 2:
            return None

        elif count == 3:
            temp = head.next
            head.next = head.next.next
            temp.next = None
            head.next.next = temp
            return None

        leng = count

        if leng%2 == 0:
            tar = leng//2 + 1
        else:
            tar = (leng+1)//2 + 1

        curr = head
        count = 1
        oddsert = None
        headn = None

        while True:
            curr = curr.next
            count = count + 1

            if leng%2 != 0  and count == tar-2:
                oddsert = curr.next
                headn = curr.next.next
                curr.next = None
                oddsert.next = None
                break

            if count == tar-1:
                headn = curr.next
                curr.next = None
                break

        prevn = headn
        currn = headn.next
        headn.next = None

        while currn.next != None:
            futn = currn.next
            currn.next = prevn
            prevn = currn
            currn = futn

        currn.next = prevn

        head2 = currn
        curr1 = head
        curr2 = head2

        while True:
            fut1 = curr1.next
            fut2 = curr2.next
            curr1.next = curr2
            curr2.next = fut1

            if fut1.next == None:
                fut1.next = fut2
                break

            curr1 = fut1
            curr2 = fut2

        if oddsert != None:
            fut2.next = oddsert
            
        return None