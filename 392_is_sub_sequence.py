class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # axc in ahfcxc = true
        # two pointers approach:
        if(len(s) == 0): return True
        elif(len(t) == 0): return False
        i,j=0,0
        result_string = []

        while j!=len(t) and i!=len(s):
            #print(f"t: {t[j]} s: {s[i]}")
            if(s[i] == t[j]):
                result_string.append(s[i])
                i+=1

            j+=1
        
        return "".join(result_string) == s

sol = Solution()
r=sol.isSubsequence("abc", "ahbgdc")
print(r)
r=sol.isSubsequence("b", "ahbgdc")
print(r)
r=sol.isSubsequence("", "ahbgdc")
print(r)
r=sol.isSubsequence("", "")
print(r)