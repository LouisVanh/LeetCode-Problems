from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available_letters = Counter(magazine)
        
        for letter in ransomNote:
            if(letter in available_letters):
                if available_letters[letter] == 0: return False
                
                available_letters[letter] -= 1
            
            else:
                return False
        
        print(available_letters)
        return True



sol = Solution()
r=sol.canConstruct("dadaadabc", "aaadbadcd")
print(r)