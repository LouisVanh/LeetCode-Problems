from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        while val in nums:
            nums.remove(val)

        print(nums)
        for i in range(cnt):
            nums.pop()

        print(nums)
        return len(nums)

sol = Solution()
re = sol.removeElement([1,3,4,5,6,9,10,12,2,2,9], 2)

print(re)
re = sol.removeElement([0,1,2,2,3,0,4,2], 2)
print(re)
