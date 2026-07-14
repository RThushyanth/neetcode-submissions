class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        if len(tickets) == 1:
            return tickets[0]


        flight_dict = {}
        
        for pair in tickets:
            if pair[0] not in flight_dict:
                flight_dict[pair[0]] = [pair[1]]
            else:
                flight_dict[pair[0]].append(pair[1])

        for key in flight_dict:
            flight_dict[key].sort(reverse=True)

        
        ans = []
        stack = []
        curr = "JFK"
        ncurr = None
        stack.append(curr)

        while flight_dict:
            if curr in flight_dict:
                ncurr = flight_dict[curr].pop()
                stack.append(ncurr)
                if flight_dict[curr] == []:
                    del flight_dict[curr]
                curr = ncurr

            else:
                while stack[-1] not in flight_dict:
                    ans.append(stack.pop())
                curr = stack[-1]

        while stack:
            ans.append(stack.pop())

        return ans[::-1]



       