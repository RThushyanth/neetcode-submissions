class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        from collections import deque

        dlist = deque([])
        result = []

        #initialize

        dlist.append(0)

        for i in range(1,k):
            if nums[i] > nums[dlist[-1]]:
                while dlist != deque([]) and nums[i] > nums[dlist[-1]]:
                    dlist.pop()
                dlist.append(i)

            else:
                dlist.append(i)

        result.append(nums[dlist[0]])

        #sliding

        left_pointer = 0
        right_pointer = k-1 

        while right_pointer < len(nums)-1:
            if nums[left_pointer] == nums[dlist[0]]:
                dlist.popleft()
            left_pointer = left_pointer + 1

            if dlist == deque([]):
                dlist.append(right_pointer+1)

            elif nums[right_pointer + 1] > nums[dlist[-1]]:
                while dlist != deque([]) and nums[right_pointer + 1] > nums[dlist[-1]]:
                    dlist.pop()
                dlist.append(right_pointer+1)
            else:
                dlist.append(right_pointer+1)
            
            right_pointer = right_pointer + 1

            result.append(nums[dlist[0]])

        return result



        