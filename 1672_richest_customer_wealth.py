from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for person in accounts:
            max_sum = max(max_sum, sum(person))
        
        return max_sum
    

sol = Solution()
r=sol.maximumWealth([[1,2,3],[3,2,2]])
print(r)