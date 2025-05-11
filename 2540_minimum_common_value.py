from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1)&set(nums2)
        return min(intersection) if intersection else -1
    
sol=Solution()
r=sol.getCommon([1,2,3], [2,4,1])
print(r)