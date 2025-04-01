class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = []
        min_length = min(len(word1),len(word2))
        for i in range(min_length):
            new_word.append(word1[i])
            new_word.append(word2[i])
        
        if len(word1) == len(word2): return "".join(new_word)
        longest = word1 if len(word1) > len(word2) else word2
        return "".join(new_word) + longest[min_length:]

sol = Solution()
r = sol.mergeAlternately("abc","pqr")
print(r)
r = sol.mergeAlternately("","pqr")
print(r)
r = sol.mergeAlternately("abcaaaaaaaaab","p")
print(r)
r = sol.mergeAlternately("","")
print(r)