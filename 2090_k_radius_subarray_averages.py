from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result_arr = []
        n = len(nums)
        sum = 0

        # 0 1 2 3 4 5 6 7
        # k = 2
        # n = 8 --> n-k = 6 --> must use >= because 6 should also be -1
        # i-k =
        if k == 0:
            return nums
        
        for i in range(-k, n):
            # sum logic:
            # add it to the sum for sliding window
            if(i+k < n):
                sum+=nums[i+k]
            # if k is 2, we want to discard our previous left bound away (first time: index 3 --> discard index 0) = i - k - 1
            if(i-k-1 >= 0):
                sum-=nums[i-k-1]

            # -1 logic
            if (i < k) or (i >= n-k):
                # first k elements... can't make average (or last k elements)
                if(i>=0):
                    result_arr.append(-1)

            else:
                result_arr.append(sum//(2*k+1))

        return result_arr
    
sol = Solution()  #0 1 2 3 4 5 6 7 8
r=sol.getAverages([7,4,3,9,1,8,5,2,6], 3)
print(r)