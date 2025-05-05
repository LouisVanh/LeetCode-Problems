from collections import Counter
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        unique = set()
        print(count)

        for i in count:
            # print(i)
            print(f"i is {i} and the count[i] is {count[i]}")
            if count[i] in unique:
                return False
            else:
                unique.add(count[i])

        return True



sol = Solution()
r=sol.uniqueOccurrences([1,2,2,3,3,4,-1,5,5,5,6])
# r=sol.uniqueOccurrences([1,2,4,4,5])
print(r)