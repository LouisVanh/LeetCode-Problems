from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        triplets = 0
        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if(abs(arr[i] - arr[j]) > a):
                    continue

                for k in range(j+1, len(arr)):
                    if(abs(arr[j] - arr[k]) > b):
                        continue

                    if(abs(arr[i]-arr[k]) > c):
                        continue

                    triplets+=1

        return triplets

sol = Solution()
r=sol.countGoodTriplets([3,0,1,1,9,7], 7,2,3)
print(r)