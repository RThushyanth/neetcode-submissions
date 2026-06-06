# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        curr = head
        leng = 1

        while curr.next:
            curr = curr.next
            leng = leng + 1

        if leng < k:
            return head

        revno = leng//k
        remno = leng - k*revno

        plast = None
        thead = head
        headn = None

        if k >=3:

            while revno != 0:

                count = 0
                prev = thead
                curr = thead.next
                thead.next = None

                while True:
                    fut = curr.next
                    curr.next = prev
                    count = count + 1
                    prev = curr
                    curr = fut
                    if count == k-2:
                        if plast != None:
                            plast.next = curr

                        plast = thead

                        if curr.next != None:
                            thead = curr.next

                        curr.next = prev

                        if revno == leng//k:
                            headn = curr

                            
                        break
                        
                revno = revno - 1
            
            if remno != 0:
                plast.next = thead

        elif k == 2:
            if revno >= 1:
                headn = head.next
            theadn = head
            while revno != 0:
                thead = theadn
                while True:
                    temp = thead.next
                    if temp.next == None:
                        temp.next = thead
                        thead.next = None
                        break
                    theadn = temp.next
                    temp.next = thead
                    if remno !=0 and revno == 1:
                        thead.next = theadn
                        break
                    thead.next = theadn.next
                    break
                revno = revno-1


        else:
            return head


        return headn
            
        
            



            

        
        