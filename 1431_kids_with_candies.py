from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # candies_needed_to_have_the_most = max(candies) - extraCandies + 1
        # return [x>=candies_needed_to_have_the_most for x in candies]
        return [x>=(max(candies) - extraCandies) for x in candies]


sol = Solution()
r=sol.kidsWithCandies([4,2,1,1,2], 1)
print(r)