from typing import List
#Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
#In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
#Note that 0 is neither positive nor negative.

class Solution:
    def maximumCountBruteForce(self, nums: List[int]) -> int:
        pos_numbers_count, neg_numbers_count = 0, 0
        for i in range(len(nums)):
            if(nums[i] > 0):
                pos_numbers_count+=1
            if(nums[i] < 0):
                neg_numbers_count+=1
        
        if(pos_numbers_count > neg_numbers_count):
            return pos_numbers_count
        else: return neg_numbers_count

    #more optimised version (checks only half)
    def maximumCount(self, nums: List[int]) -> int:
        negative_count = 0
        zero_count = 0
        for i in range(len(nums)):
            if(nums[i] < 0):
                negative_count+=1
            elif(nums[i] == 0):
                zero_count+=1

        if(zero_count > 0):
            if(negative_count >= (len(nums)-zero_count) /2):
                return negative_count
            else: return len(nums)-zero_count - negative_count
        
        else: # no zeros
            if(negative_count >= len(nums)/2):
                return negative_count
            else: return len(nums) - negative_count

sol = Solution()
result = sol.maximumCountBruteForce([-1, -2, -3, 0, 2, 4, 69])
result = sol.maximumCount([-1, -2, -3, -4, 2, 4, 69])
print(result)