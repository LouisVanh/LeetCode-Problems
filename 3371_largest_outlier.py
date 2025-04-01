from typing import List
import math
from collections import Counter
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # n-2 numbers together make one number, the other number is irrelevant.
        # find this number.
        # that means that, if we pop one element at random
        counter = Counter(nums)
        total_sum = sum(nums)
        nums_lookup = set(nums)
        largest = -math.inf
        for i in range(len(nums)):
        # sum up the entire array
            if(nums[i] < largest): continue
            if(counter[nums[i]] == 1):
                nums_lookup.remove(nums[i])
            interval_sum = total_sum - nums[i]

            # it must be equal to 2 * some element in that array
            if(interval_sum/2 in nums_lookup):
                largest = nums[i]

            if(counter[nums[i]] == 1):
                nums_lookup.add(nums[i])

        return largest

sol = Solution()
r = sol.getLargestOutlier([2,3,5,10])
print(r)