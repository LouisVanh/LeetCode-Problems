from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # approach:
        # check if the same letters are used. this is a prerequisite.
        if (set(word1) != set(word2)):
            return False
        
        # check whether or not the sorted counter values of both are the same, if yes, we can mutate it to be the same in ... operations
        counter1, counter2 = Counter(word1), Counter(word2)
        # print(counter1.values)
        sorted1, sorted2 = sorted(list(counter1.values())), sorted(list(counter2.values()))
        # print(f"sorted1 is {sorted1}")
        # print(f"sorted2 is {sorted2}")

        # order is irrelevant so no need to even check for this
        return sorted1 == sorted2
    

sol = Solution()
r=sol.closeStrings("sara", "aras")
print(r)
r=sol.closeStrings("sara", "louis")
print(r)
r=sol.closeStrings("abc", "abcc")
print(r)
r=sol.closeStrings("abc", "cba")
print(r)