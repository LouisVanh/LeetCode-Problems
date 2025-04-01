from typing import List
import math
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Given a list of sorted distinct integers, find the index where some element should be
        mid = math.floor(len(nums)/2)
        left = 0
        right = len(nums)-1
        print(f"mid is {mid}")
        # Found the index
        if(target in nums):
            return nums.index(target)
        
        while True:
            if(target < nums[mid]):
                right = mid
                mid = math.floor((right-left)/2) + left
                print(f"I'm smaller than the mid value, right bounds adjusted! mid: {mid}; right: {right}, left: {left}")
                if(right-left <= 1):
                    print("The left and right index are right next to eachother, but the target is none of them. It must be inserted <")
                    if(target<nums[left]):
                        return left
                    elif(target<nums[right]):
                        return right
                    else: return right+1

            elif(target > nums[mid]):
                left = mid
                mid = math.floor((right-left)/2) + left
                print(f"I'm bigger than the mid value, , left bounds adjusted! mid: {mid}; right: {right}, left: {left}")
                if(right-left <= 1):
                    print("The left and right index are right next to eachother, but the target is none of them. It must be inserted >")
                    if(target<nums[left]):
                        return left
                    elif(target<nums[right]):
                        return right
                    else: return right+1


sol = Solution()
# r = sol.searchInsert([1,3,5,6], 4)
# print(r)
# r = sol.searchInsert([1,3,5,6], 7)
# print(r)
# r = sol.searchInsert([1,3,5,6], 2)
# print(r)
# r = sol.searchInsert([1,3,5,6], 3)
# print(r)
# r = sol.searchInsert([1,3,5,6], 0)
# print(r)
r = sol.searchInsert([1], 0)
print(r)
r = sol.searchInsert([1,3], 1)
print(r)