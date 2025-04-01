from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # two pointers approach, but can also be done with hashmap
        # sorting to make two pointers possible without brute forcing double for loop
        nums.sort()
        result = 0
        i,j=0, len(nums)-1
        print(nums)
        while i<j:
            print(f"i is {i}, j is {j}")
            if(nums[i] + nums[j] == k):
                result+=1
                i+=1
                j-=1
            # NO MATCH FOUND!
            else: # keep incrementing / decrementing
                if(nums[i] + nums[j] > k):
                    # too much! remove end
                    j-=1
                else:
                    i+=1


        return result
    
sol = Solution()
# r=sol.maxOperations([1,2,3,4,3,1,2], 5)
# print(r)
r=sol.maxOperations([3,1,3,4,3, 5], 6)
print(r)