from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers, get max area of rect
        # start at ultimates
        i,j=0, len(height)-1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
            if(height[i] < height[j]):
                i+=1
                while(height[i] < height[i-1]):
                    i+=1
                    if(i==j): return max_area
            else:
                j-=1
                while(height[j] < height[j+1]):
                    j-=1
                    if(i==j): return max_area

        return max_area
    
sol = Solution()
r=sol.maxArea([1,8,6,2,5,4,8,3,7])
print(r)
r=sol.maxArea([2,4,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print(r)