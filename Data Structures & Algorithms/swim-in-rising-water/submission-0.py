class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        import heapq

        n = len(grid)

        visited_set = set()
        minheap = []
        minheap.append((0,(0,0)))
        time = 0

        while (n-1,n-1) not in visited_set:
            curr = heapq.heappop(minheap)
            if curr[1] in visited_set:
                continue
            celav = grid[curr[1][0]][curr[1][1]]
            if celav > time:
                time = celav
            visited_set.add(curr[1])

            if curr[1][0] != 0:
                elav = grid[curr[1][0]-1][curr[1][1]]
                if (curr[1][0]-1,curr[1][1]) not in visited_set:
                    if elav > time:
                        heapq.heappush(minheap,(elav,(curr[1][0]-1,curr[1][1])))
                    else:
                        heapq.heappush(minheap,(0,(curr[1][0]-1,curr[1][1])))

            if curr[1][0] != n-1:
                elav = grid[curr[1][0]+1][curr[1][1]]
                if (curr[1][0]+1,curr[1][1]) not in visited_set:
                    if elav > time:
                        heapq.heappush(minheap,(elav,(curr[1][0]+1,curr[1][1])))
                    else:
                        heapq.heappush(minheap,(0,(curr[1][0]+1,curr[1][1])))

            if curr[1][1] != 0:
                elav = grid[curr[1][0]][curr[1][1]-1]
                if (curr[1][0],curr[1][1]-1) not in visited_set:
                    if elav > time:
                        heapq.heappush(minheap,(elav,(curr[1][0],curr[1][1]-1)))
                    else:
                        heapq.heappush(minheap,(0,(curr[1][0],curr[1][1]-1)))

            if curr[1][1] != n-1:
                elav = grid[curr[1][0]][curr[1][1]+1]
                if (curr[1][0],curr[1][1]+1) not in visited_set:
                    if elav > time:
                        heapq.heappush(minheap,(elav,(curr[1][0],curr[1][1]+1)))
                    else:
                        heapq.heappush(minheap,(0,(curr[1][0],curr[1][1]+1)))
            

        return time

        