from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        numbers = [x for row in grid for x in row]
        isPossible = all([a%x==numbers[0]%x for a in numbers])
        if not isPossible: return -1

        # Sort numbers to get the median value
        numbers.sort()
        median = (numbers[len(numbers)//2])
        total_ops = 0
        for i in numbers:
            total_ops+= abs(i-median)/x 

        return total_ops
        


sol = Solution()
r=sol.minOperations([[2,4],[6,8]], 2)
print(r)