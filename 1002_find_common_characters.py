from typing import List
from collections import Counter
class Solution:
    # Since the question wants us to include duplicates, we cannot just use a normal set, or "aa" and "aab" will return "a" when we expect "a","a"
    # def commonChars(self, words: List[str]) -> List[str]:
        # result_set = set(words[0])
        # for word in words:
        #     result_set = result_set & set(word)
        #     print(f"{result_set} is the result set after '{word}'")

        # return list(result_set)

    def commonChars(self, words: List[str]) -> List[str]:
        result_counter = Counter(words[0])
        for word in words:
            result_counter = result_counter & Counter(word)
            # print(f"{result_counter} is the result set after '{word}'")

        result_list = list()
        for char in result_counter:
            #don't do this: it's not faster and more space intense:
            #result_list.extend(char * result_counter[char])
            for _ in range(result_counter[char]):
                result_list.append(char)
        
        return result_list

sol = Solution()
# r = sol.commonChars(["bella","label","roller"])
r = sol.commonChars(["aabb","abbc","abbcccddddeeeee"])
print(r)