from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # We just need to find any peak element (= element where left and right is smaller than it)
        # outside of array = -inf
        # needs to be within big O log(n), so no sorting. let's do two pointer
        i,j = 0, len(nums)-1

        # edge cases: bounds
        if(nums[0] > nums[1]):
            print("early")
            return nums[0]
        elif(nums[j] > nums[j-1]):
            print("late")
            return nums[j]
        
        while True:
            i+=1
            j-=1
            print(f"i:{i}; j:{j}")
            if(nums[i-1] < nums[i] and nums[i] > nums[i+1]):
                return i
            
            if(nums[j-1] < nums[j] and nums[j] > nums[j+1]):
                return j
        
        return -1
    
sol = Solution()
r=sol.findPeakElement([1,2,3,1])
print(r)