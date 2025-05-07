from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        max_count = 0
        zero_count = 0
        left,right = 0,0
        while right < n:
            if nums[right] == 0:
                # use up all of our k's, always
                zero_count+=1

                # shrink window when we use too many zeroes
                while(zero_count > k):
                    if(nums[left] == 0):
                        zero_count-=1

                    left+=1

            # default case: we find a 1 and just expand the window
            right+=1
            max_count = max(max_count, right-left)
        return max_count


sol = Solution()
r=sol.longestOnes([1,1,1,1], 1)
r2=sol.longestOnes([1,1,0,1,1], 1)
r3=sol.longestOnes([1,1,0,0,0,1,1], 1)
r4=sol.longestOnes([0,0,0,0,0], 1)
r5=sol.longestOnes([0,0,0,0,0], 5)
r6=sol.longestOnes([0,0,0,0,0], 0)
print(r)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)

