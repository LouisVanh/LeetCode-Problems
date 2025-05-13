from typing import List
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        set_of_numbers = set()
        counter = Counter(digits)

        for third_digit in digits:
            if(counter[third_digit] <= 0) or third_digit % 2 != 0: continue # even check and freq check
            counter[third_digit]-=1

            for available_first_digit in counter:
                if(counter[available_first_digit] <= 0) or available_first_digit == 0: continue # 0 start check and freq check
                counter[available_first_digit]-=1

                for available_second_digit in counter:
                    if(counter[available_second_digit] <= 0): continue
                    set_of_numbers.add(100*available_first_digit + 10*available_second_digit + third_digit)

                counter[available_first_digit] += 1

            counter[third_digit]+=1

        return sorted(list(set_of_numbers))
    
sol = Solution()
r=sol.findEvenNumbers([2,3,1,0])
print(r)