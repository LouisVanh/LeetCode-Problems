from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique_in_nums1 = set()
        unique_in_nums2 = set()
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        for i in set_nums1:
            if i not in set_nums2:
                unique_in_nums1.add(i)

        for i in set_nums2:
            if i not in set_nums1:
                unique_in_nums2.add(i)
                
        return [list(unique_in_nums1),list(unique_in_nums2)]
    
    
sol = Solution()
r=sol.findDifference([1,2,3,4,4], [2,3,4,5])
print(r)