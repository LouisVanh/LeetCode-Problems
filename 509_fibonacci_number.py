class Solution:
    def fib(self, n: int) -> int:
        if(n <=1): return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
sol = Solution()
r=sol.fib(7)
print(r)
r=sol.fib(6)
print(r)
r=sol.fib(5)
print(r)
r=sol.fib(4)
print(r)