from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_operations = 0
        zero_count = nums.count(0)
        # The flipping that we have to do
        def flip3(starting_index):
            nonlocal min_operations
            nonlocal zero_count
            for i in range(3):
                if(nums[starting_index + i] == 0):
                    zero_count-=1 # We swap a zero, so put the count of zeros one lower
                    nums[starting_index + i] = 1
                    # print(f"Zeros: {zero_count}")
                else: 
                    zero_count+=1 # New zero created
                    nums[starting_index + i] = 0

            min_operations+=1

        # if list is 1 1 1 1 0 x, we cannot possibly fix it. Out of elements at the end.
        for i in range(len(nums)-2):
            if(nums[i] == 0):
                flip3(i)
                # print(nums)

            if(zero_count == 0):
                return min_operations
        
        return -1

            



sol = Solution()
r = sol.minOperations([0,1,1,1,0,0])
print(r)