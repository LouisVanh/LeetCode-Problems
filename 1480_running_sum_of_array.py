from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        running_sum_list = []
        # single pass through list
        for i in nums:
            prefix_sum+=i
            running_sum_list.append(prefix_sum)
        return running_sum_list

sol = Solution()
r=sol.runningSum([1,1,1,1,1])
print(r)