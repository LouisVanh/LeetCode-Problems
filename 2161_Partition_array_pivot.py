from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, count_of_pivots = [], [], 0
        for i in nums:
            if(i < pivot): left.append(i)
            elif (i> pivot): right.append(i)
            else: count_of_pivots+=1

        return left + [pivot] * count_of_pivots + right
    
sol = Solution()
r=sol.pivotArray([9,12,5,11,14, 3], 10)
print(r)
r=sol.pivotArray([-3,4,3,2],2 )
print(r)
