from typing import List
from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right_side = Counter(nums)
        left_side = Counter()
        n = len(nums)
        idx=0
        for value in nums:
            right_side[value] -= 1
            left_side[value] += 1
            if(left_side[value] * 2 > idx+1 and right_side[value] * 2 > n-idx-1):
                return idx
                
            idx+=1

        return -1
    

sol = Solution()
r=sol.minimumIndex([1,2,2,2])
print(r)