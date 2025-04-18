class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n==1):
            return True
        elif(n<1 or n%2!=0):
            return False
        
        return self.isPowerOfFour(n/4)
    
sol = Solution()
r=sol.isPowerOfFour(64)
print(r)