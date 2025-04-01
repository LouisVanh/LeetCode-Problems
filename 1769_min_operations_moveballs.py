from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n, left_count, right_count, left_cost, right_cost = len(boxes),0,0,0,0
        answer = [0] * n
        for box in range(1, n):
            # Increment left count to update amount of 1s to move
            if(boxes[box-1] == "1"): left_count +=1
            # Move all of the previous ones up by 1
            left_cost += left_count
            answer[box] = left_cost

        for box in range(n-2, -1, -1):
            # Increment right count to update amount of 1s to move
            if(boxes[box+1] == "1"): right_count +=1
            # Move all of the previous ones up by 1 (right_count * 1 = right_count)
            right_cost += right_count
            # Instead of checking per box, we loop through the entire list and do left + right. Counter intuitive, but correct.
            answer[box] += right_cost
 
        return answer