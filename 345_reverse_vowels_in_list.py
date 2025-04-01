class Solution:
    def reverseVowels(self, s: str) -> str:
        positions = []
        vowels = []
        vowels_allowed = set("aeiouAEIOU")  # faster lookup than list
        for i, char in enumerate(s):
            if(char in vowels_allowed):
                vowels.append(char)
                positions.append(i)

        vowels.reverse()
        new_string_chars = list(s)

        for i, pos in enumerate(positions):
            new_string_chars[pos]= vowels[i]
        
        return "".join(new_string_chars)

sol = Solution()
r=sol.reverseVowels("leEtcode")
print(r)
r=sol.reverseVowels("IceCreAm")
print(r)
r=sol.reverseVowels("a")
print(r)