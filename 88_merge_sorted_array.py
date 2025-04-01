from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            # print(i)
            nums1[m+i] = nums2[i]
        nums1.sort()
        # print(nums1)

s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)