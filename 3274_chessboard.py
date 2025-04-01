class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        num1 = int(ord(coordinate1[0]) - ord('a') + 1) # formula for alphabet number
        num2 = int(coordinate1[1])
        num3 = int(ord(coordinate2[0]) - ord('a') + 1) # formula for alphabet number
        num4 = int(coordinate2[1])

        if((num1 + num2) % 2 == ((num3 + num4) % 2)):
            return True
        else: return False

sol = Solution()
re = sol.checkTwoChessboards("a1", "a2")
print(re)
re = sol.checkTwoChessboards("a1", "c5")
print(re)
re = sol.checkTwoChessboards("a1", "c6")
print(re)