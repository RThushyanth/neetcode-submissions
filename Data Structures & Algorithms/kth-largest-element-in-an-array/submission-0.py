class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return nums[0]

        import heapq
        
        minheap = nums[0:k]

        heapq.heapify(minheap)

        for i in range(k,len(nums)):
            if nums[i] > minheap[0]:
                heapq.heapreplace(minheap,nums[i])
        
        return minheap[0]