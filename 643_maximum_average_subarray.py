from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_of_window = max_sum = sum(nums[:k])
        # print((nums[:k]))
        for i in range(k, len(nums)):
            sum_of_window += nums[i] - nums[i-k]
            max_sum = max(sum_of_window, max_sum)

        return max_sum/k


sol = Solution()
r = sol.findMaxAverage([1,12,-5,-6,50,3], 4)
print(r)