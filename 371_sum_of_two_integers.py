class Solution:
    def getSum(self, a: int, b: int) -> int:
        print(bin(a))
        print(bin(b))
        print(f"{a&b}: {bin(a^b)}")



            

sol = Solution()
r=sol.getSum(5, 5)
print(r)
