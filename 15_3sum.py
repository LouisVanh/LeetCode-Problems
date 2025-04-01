from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        i = -1
        n = len(nums)
        while (i != n-3):
            i+=1
            if(nums[i] > 0): break
            if(i > 0 and nums[i] == nums[i-1]): continue

            # TWO POINTERS!
            j, k = i+1, n-1
            while (j < k):
                total = nums[i] + nums[j] + nums[k]
                if(total == 0):
                    results.append([nums[i], nums[j], nums[k]])

                    # Remove duplicates
                    while(j<k and nums[j] == nums[j+1]): 
                        j+=1
                        
                    while(j<k and nums[k] == nums[k-1]): 
                        k-=1

                    j+=1
                    k-=1
                
                elif total <= 0:
                    # Total's too small, move up j
                    j+=1
                elif total >= 0:
                    # Total's too large, move up k
                    k-=1

        return results

sol = Solution()
r = sol.threeSum([-1,-1,0,1,2,-1,-4])
print(r) 
# r = sol.threeSum([0,0,0])
# print(r) 