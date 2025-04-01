from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total_spots = 0
        if(n==0): return True
        flowerbed_length = len(flowerbed)
        if(len(flowerbed) < 3):
            if (1 in flowerbed):return False
            else: total_spots = 1
        
        else:
            # When is a flower non adjacent? having 000 next to eachother is +1, having 00 start or 00 end is +1,
            # Starting 00
            if(flowerbed[0] == 0 and flowerbed[1] == 0):
                flowerbed[0] = 1
                total_spots+=1
            
            # Ending 00
            if(flowerbed[flowerbed_length-1] == 0 and flowerbed[flowerbed_length-2] == 0):
                flowerbed[flowerbed_length-1] = 1
                total_spots+=1

            # 000
            i = 1
            while i != flowerbed_length-2:
                if(flowerbed[i] == 0):
                    if(flowerbed[i+1] == 0):
                        if(flowerbed[i+2] == 0):
                            flowerbed[i+1] = 1
                            total_spots+=1
                        

                i+=1

        return total_spots>=n

sol = Solution()
r=sol.canPlaceFlowers([1,0,1,0,0,0,1], 2)
print(r)
r=sol.canPlaceFlowers([0,0], 2)
print(r)
r=sol.canPlaceFlowers([0,1], 1)
print(r)
r=sol.canPlaceFlowers([0,0,0,1,0], 2)
print(r)