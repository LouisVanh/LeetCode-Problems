class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Twwo pointer approach:
        i, j = 0, len(s)-1

        #If i and j are the same, then remove them from the string (turned into a list for performance)
        word = list(s)
        while len(word) > 1:
            if(word[i]==word[j]):
                word.pop(j)
                word.pop(i)
                j-=2
                print(f"did some popping (i:{i}, j:{j}), remaining: " + str(word))
            
            else:
                # uh oh, something's not the same.
                # Let's try naively removing one, seeing if it's a palindrome, and if not, try it for the other one.
                removed = word.pop(i)
                reversed_word = [word[-x] for x in range(1,len(word)+1)]
                print(reversed_word)
                print(word)
                if(word == reversed_word):
                    # print("word is = reversed")
                    return True
                
                else:
                    word.insert(i, removed)
                    word.pop(j)
                    reversed_word = [word[-x] for x in range(1,len(word)+1)]
                    if(word == reversed_word):
                        #print("word is = reversed")
                        return True
                    else: return False

        # If only one letter is left, it's a valid palindrome
        # print("end")
        return True

sol = Solution()
# r= sol.validPalindrome("aba")
# print(r)
# r= sol.validPalindrome("abca")
# print(r)
r= sol.validPalindrome("abc")
print(r)