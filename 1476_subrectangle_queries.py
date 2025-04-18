from typing import List
class SubrectangleQueries:
    matrix = [[]]
    def __init__(self, rectangle: List[List[int]]):
        self.matrix = rectangle
        return

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range (row1, row2+1):
            for col in range(col1,col2+1):
                self.matrix[row][col] = newValue
        return

    def getValue(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
obj = SubrectangleQueries(rectangle=[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]])
obj.updateSubrectangle(0,1,2,2,4)
print(obj)