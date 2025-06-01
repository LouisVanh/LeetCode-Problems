from typing import List
from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        common_uniques = set()
        print(count1)
        for i in count1:
            if(count1[i] == 1 and count2[i] == 1):
                print(i)
                common_uniques.add(i)
            # print(f"i is {i}, j is {count1[i]}")

        return len(common_uniques)

sol = Solution()
r=sol.countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"])
print(r)