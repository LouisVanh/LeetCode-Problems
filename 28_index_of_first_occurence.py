class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle) > len(haystack)):
            return -1
        # Let's do it with sliding window for practice:
        # the window size is always the length of the needle
        window_size = len(needle)
        print(window_size)
        # Define first window boundaries
        i, j = 0, window_size-1

        # Loop through the window
        while(j!=len(haystack)):
            print(f"{i} - {j}")
            if(haystack[i] != needle[0]):
                # First letters not even correct, move window
                print("First letters not even correct")
                i+=1
                j+=1
                continue
            
            # Okay, first letters right, check the other letters
            can_continue = True
            for a in range(1, window_size):
                if(haystack[i+a] != needle[a]):
                    # Letter incorrect, move window
                    print(f"Close, but letter at spot {a} is incorrect")
                    i+=1
                    j+=1
                    can_continue = False
                    break
            if(can_continue):
                return i
        # Couldn't find the needle.
        return -1

sol = Solution()
re = sol.strStr("bsssssadbutsad", "sad")
print(re)
re = sol.strStr("bsssssadbutsad", "sadbutsad")
print(re)