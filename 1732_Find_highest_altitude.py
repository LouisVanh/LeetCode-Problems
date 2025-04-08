from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum, max_num = 0, 0
        for i in gain:
            prefix_sum+=i
            max_num = max(max_num, prefix_sum)
        
        return max_num
    
sol = Solution()
r=sol.largestAltitude([-5,1,5,0,-7])
print(r)
r=sol.largestAltitude([-4,-3,-2,-1,4,3,2])
print(f"{r} is largest")