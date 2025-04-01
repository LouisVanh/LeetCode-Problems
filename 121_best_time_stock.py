from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # SLIDING WINDOW AND TWO POINTERS TIME
        # MAXIMIZE DIFF BETWEEN I AND J
        i, j, largest_profit = 0, 0, 0

        while True:

            # Stopping condition:
            if(j == len(prices)-1):
                return largest_profit
            
            # Sliding window j
            j += 1
            
            # Find smallest i before j (keeping the old one if the new one isn't smaller)
            if(prices[j-1] < prices[i]):
                i = j-1

            # Calculate difference, save if bigger
            if(prices[j] - prices[i] > largest_profit):
                largest_profit = prices[j] - prices[i] 
                # print(largest_profit)

sol = Solution()
r = sol.maxProfit([7,2,20,1,10,5])
print(r)
r = sol.maxProfit([1,2])
print(r)
r = sol.maxProfit([1,2,3])
print(r)
r = sol.maxProfit([3, 2, 1])
print(r)
r = sol.maxProfit([28,29,30,2,5,21,22,1,20,18,17])
print(r)