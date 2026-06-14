class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.ln = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        import heapq
        if self.ln == 0:
            heapq.heappush(self.maxheap,-1*num)
            heapq.heappush(self.minheap,num)
        else:
            if self.ln % 2 == 0:
                if num < -1*(self.maxheap[0]):
                    heapq.heappush(self.maxheap,-1*num)
                    heapq.heappush(self.minheap,-1*self.maxheap[0])
                elif num > self.minheap[0]:
                    heapq.heappush(self.minheap,num)
                    heapq.heappush(self.maxheap,-1*self.minheap[0])
                else:
                    heapq.heappush(self.minheap,num)
                    heapq.heappush(self.maxheap,-1*num)
            else:
                if num < -1*(self.maxheap[0]):
                    heapq.heapreplace(self.maxheap,-1*num)
                elif num >= self.minheap[0]:
                    heapq.heapreplace(self.minheap,num)
        self.ln = self.ln + 1



    def findMedian(self):
        """
        :rtype: float
        """
        if self.ln % 2 == 0:
            return (-1*self.maxheap[0] + self.minheap[0])/2.0
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()