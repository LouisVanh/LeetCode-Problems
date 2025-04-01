from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        max_word_length_reached = False
        strs = sorted(strs, key=len)
        
        for letter_cnt in range(len(strs[0])):
            last_char = ""
            for word in strs:
                if(len(word) - 1 < letter_cnt):
                    max_word_length_reached = True
                    break
                
                if(last_char == ""):
                    last_char = list(word)[letter_cnt]
                    prefix+= last_char

                elif(last_char != list(word)[letter_cnt]):
                    return prefix[:-1]

            if(max_word_length_reached):
                return prefix
        # if empty
        return prefix

    
sol = Solution()
res = sol.longestCommonPrefix(["flowerrr", "floor", "fling"])
print(res)
res = sol.longestCommonPrefix(["fiona", "flowerrr", "floor", "fling"])
print(res)

res = sol.longestCommonPrefix("a")
print(res)
res = sol.longestCommonPrefix(["ab", "a"])
print(res)