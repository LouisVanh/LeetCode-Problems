from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
       if(x<0): return False
       if(str(x)==(str(x))[::-1]):
           return True
       else: return False

sol = Solution()
res = sol.isPalindrome(121)
print(res) # True
res = sol.isPalindrome(-12121)
print(res) # False