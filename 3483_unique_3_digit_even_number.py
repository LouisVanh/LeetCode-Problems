from collections import Counter
from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # for practice, doing it with recursion
        # --> recursive backtracking (dfs exploration)
        counter = Counter(digits)
        res = set()
        sol = []

        def backtrack():
            # Base case
            if len(sol) == 3:
                if sol[2] % 2 == 0:
                    res.add(tuple(sol))
                return

            # prune: if we're at 2 digits and there's no even digit left
            if len(sol) == 2 and not any(counter[d] > 0 and d % 2 == 0 for d in counter):
                return

            used = set()
            for digit in counter:
                # Cannot use this digit (none left)
                if counter[digit] == 0:
                    continue
                # prune 0 starting subsets
                if len(sol) == 0 and digit == 0:
                    continue
                # Cannot use this digit
                if digit in used:
                    continue

                used.add(digit)
                sol.append(digit)
                counter[digit] -= 1
                backtrack()
                counter[digit] += 1
                sol.pop()

        backtrack()
        return len(res)

sol = Solution()
r=sol.totalNumbers([1,2,3,4])
print(r)
r=sol.totalNumbers([6,6,6,6])
print(r)
r=sol.totalNumbers([1,3,5])
print(r)