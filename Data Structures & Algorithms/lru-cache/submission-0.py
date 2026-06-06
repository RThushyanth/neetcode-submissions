class LRUCache:

    class ListNode:
        def __init__(self,vl,nxt=None,prv=None):
            self.val = vl
            self.next = nxt
            self.prev = prv

    def __init__(self, capacity: int):
        self.dict = {}
        self.head = None
        self.end = None
        self.maxlen = capacity
        self.currlen = 0


    def get(self, key: int) -> int:
        if self.currlen == 0:
            return -1

        try:
            self.dict[key]
        except KeyError:
            return -1
        else:
            if self.currlen == 1:
                return self.dict[key][0]
            
            elif self.dict[key][1].next == None:
                return self.dict[key][0]

            elif self.dict[key][1].prev == None:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                self.end.next = temp
                temp.prev = self.end
                temp.next = None
                self.end = temp
                self.dict[key] = [self.dict[key][0],temp]
            else:
                temp = self.dict[key][1]
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = self.end
                temp.next = None
                self.end.next = temp
                self.end = temp
                self.dict[key] = [self.dict[key][0],self.end]

            return self.dict[key][0]
        

    def put(self, key: int, value: int) -> None:
        if self.maxlen == 0:
            return None

        try: 
            self.dict[key]
        except KeyError:

            if self.currlen < self.maxlen:
                if self.currlen == 0:
                    temp = self.ListNode(key)
                    self.head = temp
                    self.end = temp
                    self.currlen = 1
                else:
                    temp = self.ListNode(key)
                    self.end.next = temp
                    temp.prev = self.end
                    self.end = temp
                    self.currlen = self.currlen + 1
        
            else:
                del self.dict[self.head.val]
                temp = self.ListNode(key)
                if self.currlen > 1:
                    self.head = self.head.next
                    self.head.prev = None
                    self.end.next = temp
                    temp.prev = self.end
                elif self.currlen == 1:
                    self.head = temp
                self.end = temp
                self.currlen = self.currlen + 1

            self.dict[key] = [value,temp]

        else:
            if self.currlen == 1:
                self.dict[key] = [value,self.head]
            elif self.dict[key][1].prev == None:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                self.end.next = temp
                temp.prev = self.end
                temp.next = None
                self.end = temp
                self.dict[key] = [value,temp]
            elif self.dict[key][1].next == None:
                self.dict[key] = [value,self.end]
            else:
                temp = self.dict[key][1]
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = self.end
                temp.next = None
                self.end.next = temp
                self.end = temp
                self.dict[key] = [value,self.end]
            





        

                





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)