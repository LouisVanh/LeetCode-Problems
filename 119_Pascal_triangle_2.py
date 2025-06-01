from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        total_list = [0,1,0]
        for row in range(rowIndex):
            new_list = [0]
            for i in range(1,len(total_list)):
                new_list.append(total_list[i-1] + total_list[i])
            new_list.append(0)
            total_list=new_list
            print(f"r{row}:  {new_list}")

        return total_list[1:-1]
sol=Solution()
r=sol.getRow(3)
print(r)