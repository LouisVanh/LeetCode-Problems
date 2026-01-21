from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # given a majority element always exists
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        maj = 0,0
        for item, value in counter.items():
            if value > maj[1]:
                maj = (item,value)
        
        return maj[0]

