from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the list end-beginning
        for i in range (len(digits)-1, -1, -1):
            if(digits[i] != 9):
                digits[i] += 1
                return digits
            
            if(digits[i] == 9):
                digits[i] = 0
            
        # Got here, that means it didn't return = everything is a 9
        digits.insert(0, 1)
        return digits


sol = Solution()
r = sol.plusOne([4,3,2,1])
print(r)
r = sol.plusOne([4,3,2,1, 9, 9])
print(r)
r = sol.plusOne([9, 9, 9])
print(r)
r = sol.plusOne([9])
print(r)
r = sol.plusOne([0,0])
print(r)