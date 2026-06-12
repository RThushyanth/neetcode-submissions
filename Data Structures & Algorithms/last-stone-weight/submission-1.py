class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]

        import heapq

        L = [-x for x in stones]

        heapq.heapify(L)

        while True:
           if len(L) == 2:
            break 
           val1 = heapq.heappop(L)
           val2 = heapq.heappop(L)

           if val1 != val2:
            heapq.heappush(L,-1*abs(val1-val2))

           if len(L) == 1:
            return abs(L[0])

        if L[0] == L[1]:
            return 0
        else:
            return abs(L[0]-L[1])






        