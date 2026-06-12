class KthLargest:
    class minHeap:
        def __init__(self):
            self.heap = []
            
        def push(self,val):
            self.heap.append(val)
            childindex = len(self.heap)-1
            parindex = (childindex-1)//2
            while val < self.heap[parindex]:
                self.heap[parindex],self.heap[childindex] = self.heap[childindex],self.heap[parindex]
                if parindex == 0:
                    break
                childindex = parindex
                parindex = (parindex-1)//2

        def pop(self):
            poppedval = self.heap[0]
            self.heap[0] = self.heap[-1]
            val = self.heap.pop()
            length = len(self.heap)-1
            parindex = 0
            childindex1 = 1
            childindex2 = 2
            if childindex2 <= length:
                if self.heap[childindex1] > self.heap[childindex2]:
                    minindex = childindex2
                else:
                    minindex = childindex1
            elif childindex1 == length:
                minindex = childindex1
            else:
                minindex = 0
            while val > self.heap[minindex]:
                self.heap[parindex],self.heap[minindex] = self.heap[minindex],self.heap[parindex]
                parindex = minindex
                childindex1 = 2*parindex + 1
                childindex2 = 2*parindex + 2
                if childindex2 <= length:
                    if self.heap[childindex1] > self.heap[childindex2]:
                        minindex = childindex2
                    else:
                        minindex = childindex1
                elif childindex1 == length:
                    if val > self.heap[childindex1]:
                        self.heap[parindex],self.heap[childindex1] = self.heap[childindex1],self.heap[parindex]
                    break
                else:
                    break
            return poppedval
        
        def seek(self):
            return self.heap[0]

        def lengt(self):
            return len(self.heap)

        def poppush(self,val):
            poppedval = self.heap[0]
            self.heap[0] = val
            length = len(self.heap)-1
            parindex = 0
            childindex1 = 1
            childindex2 = 2
            if childindex2 <= length:
                if self.heap[childindex1] > self.heap[childindex2]:
                    minindex = childindex2
                else:
                    minindex = childindex1
            elif childindex1 == length:
                minindex = childindex1
            else:
                minindex = 0
            while val > self.heap[minindex]:
                self.heap[parindex],self.heap[minindex] = self.heap[minindex],self.heap[parindex]
                parindex = minindex
                childindex1 = 2*parindex + 1
                childindex2 = 2*parindex + 2
                if childindex2 <= length:
                    if self.heap[childindex1] > self.heap[childindex2]:
                        minindex = childindex2
                    else:
                        minindex = childindex1
                elif childindex1 == length:
                    if val > self.heap[childindex1]:
                        self.heap[parindex],self.heap[childindex1] = self.heap[childindex1],self.heap[parindex]
                    break
                else:
                    break
            return poppedval
    

    def __init__(self, k: int, nums: List[int]):

        self.mheap = self.minHeap()
        for i in range(0,len(nums)):
            if i <= k-1:
                self.mheap.push(nums[i])
            else:
                if nums[i] > self.mheap.seek():
                    self.mheap.poppush(nums[i])

        self.k = k

    def add(self, val: int) -> int:

        if self.mheap.lengt() == self.k:
            if val > self.mheap.seek():
                self.mheap.poppush(val)

            return self.mheap.seek()
        
        else:
            self.mheap.push(val)
            return self.mheap.seek()
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)