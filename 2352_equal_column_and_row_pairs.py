from typing import List
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # approach, check strings against eachother
        # make hashmap of rows, separated each char with a space, then make the colums with the same space separation, check against hashmap counter.
        equal_pair_count = 0
        unique_counter = Counter()
        for row in grid:
            row_string = [str(x) for x in row]
            # string_of_row = "@".join(row_string)
            string_of_row = tuple(row_string)

            # add to counter (e.g: 3 2 1)
            unique_counter[string_of_row] +=1

        for column_index in range (len(grid)):
            column = []
            for row in grid:
                column.append(str(row[column_index]))
            
            # column_string = "@".join(column)
            column_string = tuple(column)
            # print(column_string)
            # if(column_string in unique_counter and unique_counter[column_string] > 0):
            equal_pair_count+=unique_counter[column_string]
                # unique_counter[column_string]-=1

        # print(unique_counter)
        return equal_pair_count

sol = Solution()
r=sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
print(r)
r=sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
print(r)