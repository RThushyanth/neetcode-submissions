class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        import heapq

        price_dict = {}

        for detail in flights:
            if detail[0] not in price_dict:
                price_dict[detail[0]] = [(detail[2],detail[1])]
            else:
                price_dict[detail[0]].append((detail[2],detail[1]))

    
        visited_set = set()
        step_dict = {}
        minheap = []
        minheap.append((0,src,0))

        while dst not in visited_set:

            if minheap == []:
                return -1

            curr = heapq.heappop(minheap)

            if curr[1] not in step_dict:
                step_dict[curr[1]] = curr[2]
            else:
                if curr[2] < step_dict[curr[1]]:
                    step_dict[curr[1]] = curr[2]
                else:
                    continue

            visited_set.add(curr[1])

            if curr[2] == k+1:
                continue

            if curr[1] in price_dict:
                for tup in price_dict[curr[1]]:
                    heapq.heappush(minheap,(tup[0]+curr[0],tup[1],1+curr[2]))


        return curr[0]
        