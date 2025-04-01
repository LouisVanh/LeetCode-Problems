class Solution:
    def reverseWords(self, s: str) -> str:
        split_string = s.split()
        split_string.reverse()
        return " ".join(split_string)
    
sol = Solution()
r = sol.reverseWords("   the   sky is    blue")
print(r)
r = sol.reverseWords("a good   example")
print(r)
r = sol.reverseWords("  hello world  ")
print(r)