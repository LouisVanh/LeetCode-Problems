from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common_numbers = []

        # approach: find the common numbers by looping through the longest list, and taking a Counter() of the shortest. Then, updating common_numbers when the count of it is >0
        if (len(nums1) < len(nums2)):
            shortest = nums1
            longest = nums2
        else:
            shortest = nums2
            longest = nums1

        count_of_shortest = Counter(shortest)

        for i in longest:
            if i in count_of_shortest and count_of_shortest[i] > 0:
                count_of_shortest[i]-=1
                common_numbers.append(i)
        
        return common_numbers


sol = Solution()
r=sol.intersect([4,9,4,4,5], [9,4,9,8,4])
print(r)