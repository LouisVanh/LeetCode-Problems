import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # need to find the k largest element, not k largest distinct
        # can't sort (rule in question)
        # heap= []
        # for i in nums:
        #     heapq.heappush(heap, i)

        # largest = (heapq.nlargest(k, heap))
        # return largest[-1]

        # shorter:
        # heapq.heapify(nums)
        # largest = heapq.nlargest(k, nums)
        # return largest[-1]
    
        # oneliner:
        return heapq.nlargest(k, nums)[-1]

sol = Solution()
r=sol.findKthLargest([3,2,1,5,6,4], 2)
print(r)
r=sol.findKthLargest([1], 1)
print(r)
r=sol.findKthLargest([500000,500000,500000, 1, 4], 2)
print(r) 
r=sol.findKthLargest([-1,2,0], 3)
print(r) 