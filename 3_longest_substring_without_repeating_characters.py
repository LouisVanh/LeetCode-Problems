from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr, string_length = 0, len(s)
        count, max_count = 0, 0

        seen = Counter()
        seen[(s[ptr])] = 1
        if(string_length <= 1): return string_length

        while ptr < string_length-1:
            ptr+=1
            if(seen[(s[ptr])] == 0):
                count+=1
                seen[(s[ptr])] += 1
            
            else:
                #count-=1
                seen[(s[ptr])] -= 1
            
            max_count = max(count, max_count)

        return max_count
        