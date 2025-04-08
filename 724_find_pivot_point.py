from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            # check if left = right
            # print(f"i = {i} - left: {prefix_sum} - right: {total_sum-prefix_sum-nums[i]}")
            if(prefix_sum == total_sum-prefix_sum-nums[i]):
                return i
                
            prefix_sum+=nums[i]


        return -1
        
sol = Solution()
r=sol.pivotIndex([1,7,3,6,5,6])
print(r)
r=sol.pivotIndex([1,2,3])
print(r)
r=sol.pivotIndex([2,1,-1])
print(r)
r=sol.pivotIndex([1])
print(r)