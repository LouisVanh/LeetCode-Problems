from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return 1
        
        longest_sub = 1
        current_length = 1
        # Bitwise and of all elements must be equal to 0 in a continuous subarray
        # Bitwise & is 0 when there's no binary 1's in common
        # So, check starting from the start, make a sliding window:

        i, j = 0, 1

        # Loop through until j is at the very end
        while(j != len(nums)):
            # Get binary value of i
            # bin_i = bin(nums[i])
            # Get binary value of j
            # bin_j = bin(nums[j])

            # print(f"i = {i}, which is {bin_i} (={nums[i]}). j = {j}, which is {bin_j} (={nums[j]}). i&j = {nums[i]&nums[j]}")
            # if i&j != 0, i++ and reset j, and reset counter
            if(nums[i] & nums[j] != 0):
                i+=1
                j= i+1
                current_length = 1
            
            # if i&j == 0, i stays and j++, and save this as a longest sub if biggest
            else:
                # Great, i and j are compatible; BUT! All of the other elements in the subarray must also have a&b = 0
                can_continue = True
                for a in range(1, j-i):
                    if(nums[i+a] & nums[j] != 0):
                        # error! oh god. abort.
                        i+=1
                        j= i+1
                        current_length = 1
                        can_continue = False
                        break
                
                if(can_continue):
                    j+=1
                    current_length += 1
                    # print(f"Current length updated to {current_length}")
                    if(longest_sub < current_length):
                        longest_sub = current_length
        
        print("end reached")
        return longest_sub

sol = Solution()
# re = sol.longestNiceSubarray([1,3,8,48,10])
# print(re)
# re = sol.longestNiceSubarray([3,1,5,11,13])
# print(re)
# re = sol.longestNiceSubarray([1, 1, 1, 1, 2, 1, 1])
# print(re)