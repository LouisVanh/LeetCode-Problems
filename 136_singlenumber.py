from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_numbers_list = []
        for i in range(len(nums)):
            if(nums[i] not in single_numbers_list):
                single_numbers_list.append(nums[i])
            elif(nums[i] in single_numbers_list):
                single_numbers_list.pop(single_numbers_list.index(nums[i]))

        return single_numbers_list[0]
    
sol = Solution()
result = sol.singleNumber([1, 2, 3, 3, 2, 1])
print(result)