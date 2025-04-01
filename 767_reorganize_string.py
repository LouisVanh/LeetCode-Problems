import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Compile frequencies of all characters, otherwise it will be impossible to sort them correctly.
        freq_map = {}
        res = []
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
    
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)
        print(max_heap)

        # Loop through it, adding to result
        while len(max_heap) >= 2: # we're taking 2 values per time, so max one can be left

            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            res.append(char1)
            res.append(char2)

            if(freq1 + 1 < 0):
                heapq.heappush(max_heap, (freq1+1, char1))
            if(freq2 + 1 < 0):
                heapq.heappush(max_heap, (freq2+1, char2))
                
        if(max_heap):
            freq, char = heapq.heappop(max_heap)
            if(-freq > 1): return ""
            else: res.append(char)
        
        return "".join(res)

sol = Solution()
r = sol.reorganizeString("aaabcdaafghhijkl")
print(r)

                


