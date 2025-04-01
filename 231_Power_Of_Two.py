import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<0):
            return False
        binary = str(bin(n))
        print(binary)
        return binary.count("1") == 1

sol = Solution()
# print(sol.isPowerOfTwo(5))
print(sol.isPowerOfTwo(1))
# print(sol.isPowerOfTwo(12))
print(sol.isPowerOfTwo(16))
# print(sol.isPowerOfTwo(64))
# print(sol.isPowerOfTwo(-64))
print(sol.isPowerOfTwo(536870912))
print(sol.isPowerOfTwo(17179869184))
# print(sol.isPowerOfTwo("a"))

