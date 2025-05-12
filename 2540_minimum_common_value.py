from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Hashmaps
        # intersection = set(nums1)&set(nums2)
        # return min(intersection) if intersection else -1

        # using property: they are sorted asc /^

        # This is O(1) as we're doing int comparison O(1) and pointer reassignment O(1)
        if(len(nums1) > len(nums2)):
            nums1,nums2 = nums2,nums1

        set2 = set(nums2)
        for i in nums1:
            if i in set2:
                return i

        return -1
    
sol=Solution()
r=sol.getCommon([1,2,3], [2,4,1])
print(r)