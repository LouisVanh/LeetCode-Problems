from typing import List
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        small_number = nums[0]
        large_number = nums[len(nums)-1]

        gcd = 1
        for i in range(2, small_number + 1):
            print(i)
            if(small_number % i == 0 and large_number % i == 0):
                gcd = i

        return gcd

sol = Solution()
re = sol.findGCD([5,4,7,900, 8])
print(re)