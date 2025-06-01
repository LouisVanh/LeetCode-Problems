from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        freq_bucket_array = [] 
        for _ in range (len(nums)):
            freq_bucket_array.append([])
        result = []
        # First pass: setup bucket array
        for number, freq in freq_map.items():
            # Do -1 so we don't have an empty [] at the very start always (0 frequency is impossible)
            freq_bucket_array[freq-1].append(number)
        
        print(freq_bucket_array)
        # Second pass: get top k values from it
        for index in range(len(freq_bucket_array)-1, -1 ,-1):
            if(k==0): return result

            if(not freq_bucket_array[index]): continue

            for i in freq_bucket_array[index]:
                result.append(i)
                k-=1   
        
        return result
            
sol = Solution()
r=sol.topKFrequent([1,2,2,3,3,3,3,4,4,4], 2)
print(r)
r=sol.topKFrequent([1,2,2,3,3,3,3,4,4,4], 3)
print(r)
r=sol.topKFrequent([1,1,1,1,1,1],1)
print(r)
r=sol.topKFrequent([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5],5)
print(r)