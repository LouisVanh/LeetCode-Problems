from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {  "I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000   }
        
        splitted_string = list(s)
        print(splitted_string)
        cnt = 0
        prev_number = 0
        for x in splitted_string:
            if(x in roman_dict.keys()):
                if(roman_dict[x] > prev_number):
                    cnt -= 2*prev_number

                cnt += roman_dict[x]
                prev_number = roman_dict[x]
        
        return cnt
        

sol = Solution()
result = sol.romanToInt("XL")
print( result)