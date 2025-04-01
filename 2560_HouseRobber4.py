from typing import List
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
    Finds the minimum robbery capability required to rob at least k houses
    while ensuring that no two adjacent houses are robbed.

    :param nums: List of integers representing money in each house.
    :param k: Minimum number of houses to rob.
    :return: The minimum possible maximum amount stolen from a single house.
    """
    
        # Helper function to check if we can rob at least `k` houses with capability `x`
        def canRobWithCapability(x):
            count = 0  # Number of houses robbed
            i = 0  # Pointer for houses
            
            while i < len(nums):
                if nums[i] <= x:  # Can we rob this house without exceeding capability?
                    count += 1  # Rob the house
                    i += 1  # Move forward to ensure we skip the next adjacent house
                
                i += 1  # Always move to the next house
            
            return count >= k  # Return True if we can rob at least `k` houses
        
        # Binary search on the answer (minCapability)
        low, high = min(nums), max(nums)  # Possible capability range
        result = high  # Start with worst-case max
        
        while low <= high:
            mid = (low + high) // 2  # Midpoint capability to test
            
            if canRobWithCapability(mid):  
                result = mid  # Found a valid solution, try to minimize further
                high = mid - 1  # Search lower capabilities
            else:
                low = mid + 1  # Increase capability if not enough houses can be robbed
        
        return result  # Minimum capability found
    

sol = Solution()
nums = [2, 3, 5, 9]
k = 2
print(sol.minCapability(nums, k))  # Output: 5