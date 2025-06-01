from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left,right, n  = 0,0, len(nums)
        zero_index = -1
        longest_subarray_meeting_requirement = 0
        while right < n:
            print(f"Current window: {nums[left:right]} - zero is at spot {zero_index}")
            if(nums[right] == 0):
                # right ptr is currently 0.
                # we need to set our zero_index to the right pointer, after we set our left pointer to the number after our old zero, this way, a new window is made
                left = zero_index+1
                zero_index = right

            #after every iteration, we should also just move on with our right pointer

            right+=1
            longest_subarray_meeting_requirement = max(longest_subarray_meeting_requirement, right-left)
        
        # We always have to remove one, not just when there's a zero... makes it even easier
        # return longest_subarray_meeting_requirement if zero_index == -1 else longest_subarray_meeting_requirement-1
        return longest_subarray_meeting_requirement-1

sol = Solution()
r=sol.longestSubarray([0,1,1,1,0,1,1,0,1])
print(r)
