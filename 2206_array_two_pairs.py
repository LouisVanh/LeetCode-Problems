from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if(len(nums) %2 != 0):
            return False
        
        pair_dict = {}
        for i in nums:
            if(i in pair_dict.keys()):
                pair_dict.update({i: pair_dict[i]+1})
            else:
                pair_dict.update({i: 1})


        if(all(x % 2 == 0 for x in iter(pair_dict.values()))):
            return True
        
        return False

sol = Solution()
re = sol.divideArray([1,2,2,2,2,4,4])
print(re)
re = sol.divideArray([1,2,2,2,2,4,4, 1])
print(re)