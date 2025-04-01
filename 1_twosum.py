from typing import List
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []
        
    
sol = Solution()

# Call the twoSum method with a test case
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)  # Expected output: [0, 1]
result = sol.twoSum([2, 4, 8, 16, 48], 56)
print(result)  # Expected output: [2, 4]

