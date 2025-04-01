class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        while words[len(words)-1] == "":
            words.pop(len(words)-1)
        return len(words[len(words)-1])
    
sol = Solution()
re = sol.lengthOfLastWord("    Hello  World      ")
print(re)