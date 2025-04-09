class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        vowel_count, max_count = 0,0
        j = 0
        while j != len(s):
            print(f"start count of while: {vowel_count}")
            if(j < k ):
                if(s[j] in vowels):
                    vowel_count+=1

            
            # we now have a full length substring
            else:
                # j=2 : [A B C] D E --> check for i = 0 (j-2)
                # j=3 : A [B C D] E --> check for i = 1 (j-2)
                if(s[j-k] in vowels): # first letter gone (we're moving up the window)
                    vowel_count-=1
                    print(f"vowel decreased! {s[j-k]} - count: {vowel_count}")
                if(s[j] in vowels): # last letter added (moving up)
                    vowel_count+=1
                    print(f"vowel increased! {s[j]} - count: {vowel_count}")
                
            max_count = max(max_count, vowel_count)
            j+=1

        return max_count
    
sol = Solution()
r = sol.maxVowels("alphamale", 3)
print(r)