import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # one liner (log)
        #return True if (n>0 and abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10) else False
    
        # recursion:
        if(n==1):
            return True
        elif(n<1):
            return False
        
        return self.isPowerOfThree(n/3)
sol = Solution()
r=sol.isPowerOfThree(244)
print(r)