class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Phase 1: Interweave the lists (Orig1 -> Copy1 -> Orig2 -> Copy2)
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Phase 2: Assign random pointers for the copies
        curr = head
        while curr:
            if curr.random:
                # The copy's random is the node immediately after the original's random
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Phase 3: Untangle the lists and completely restore the original
        curr = head
        copy_head = head.next
        
        while curr:
            copy_node = curr.next
            # Restore the original list's next pointer
            curr.next = copy_node.next
            # Connect the copy list's next pointer
            if copy_node.next:
                copy_node.next = copy_node.next.next
            
            curr = curr.next

        return copy_head