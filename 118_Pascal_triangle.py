from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        total_list = [[0,1,0]]
        for row in range(1,numRows):
            print("row ",row)
            new_list = [0]
            for i in range(len(total_list[row-1])-1):
                new_list.append(total_list[row-1][i]+total_list[row-1][i+1])

            new_list.append(0)
            print("new:", new_list)
            total_list.append(new_list)


        for pascal_row_idx in range(len(total_list)):
            print (total_list[pascal_row_idx])
            total_list[pascal_row_idx] = total_list[pascal_row_idx][1:-1]
        return total_list

sol = Solution()
r=sol.generate(5)
print(r)