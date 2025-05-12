from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result_set = set(nums[0])
        for arr in range(1, len( nums )):
            result_set = result_set & set(nums[arr])
            # print(result_set)

        return sorted(result_set)
    

sol = Solution()
r=sol.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])
print(r)