from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals
        #  return an array of the non-overlapping intervals that cover all the intervals in the input.

        # Basic premise: sort intervals, then check if last element = first element of next, merge if true (grab min and max)
        # Let's try to do it in-place to reduce space complexity
        intervals.sort()
        i=0
        while i < len(intervals)-1:
            print(f"i: {i}, interv= {intervals}")
            if(intervals[i][1] >= intervals[i+1][0]):
                #intervals[i][0] will always stay the same (sorted)
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i+=1
        
        return intervals

sol = Solution()
r=sol.merge([[1,3],[2,6],[8,10],[15,18]])
print(r)
r=sol.merge([[1,4],[4,5]])
print(r)