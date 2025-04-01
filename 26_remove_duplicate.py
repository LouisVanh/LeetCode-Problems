from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # The array is sorted, so we can keep track of the current number
        # If we encounter this same number again, we will pop it, otherwise, there's a new current number
        # Use i simply as a max operation counter, don't use it for the value (the size of the array will change)
        # Instead, manually keep track of the position we're at with a 2nd pointer
        current_number = None
        current_loop_index = 0
        for i in range(len(nums)):
            # print(current_loop_index)
            if(nums[current_loop_index] != current_number):
                # new number, don't remove
                current_number = nums[current_loop_index]
                current_loop_index+=1
                print(f"New correct number: {current_number} and loop idx is now {current_loop_index}")
            else:
                # duplicate, gtfo
                nums.pop(current_loop_index)
        
        print(nums)
        return len(nums)



sol = Solution()
re = sol.removeDuplicates([1,1,2])
print(re)
re = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(re)