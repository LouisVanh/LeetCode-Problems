#https://leetcode.com/problems/remove-letter-to-equalize-frequency/
class Solution:
    def equalFrequency(self, word: str) -> bool:
        frequencies = {}
        for x in word:
            if(x not in frequencies.keys()):
                frequencies.update({x: 1})
            elif(x in frequencies.keys()):
                frequencies.update({x: frequencies[x]+1})

        #print(frequencies)
        keys_list = list(frequencies.keys())
        for x in keys_list:
            # Remove one from a frequency, check if they're all the same
            if(frequencies[x] != 1):
                frequencies.update({x: frequencies[x]-1})
                lost_value = False
                
            # If there's only one letter, pop it out!
            else:
                # print("removing letter" + str(x))
                frequencies.pop(x)
                lost_value = True

            # print(frequencies)
            # Generate a new list with all booleans, checking if the elements are equal to the first element (= all the same)
            values_list = list(frequencies.values())
            first_val = values_list[0]
            if all(y == first_val for y in values_list):
                 # If now all of the freq are the same, return true
                return True
            else: # fix the dict again
                if(lost_value == False):
                    frequencies.update({x: frequencies[x]+1})
                else:
                    frequencies.update({x: 1})
                    lost_value = False

        return False       
    
sol = Solution()
res = sol.equalFrequency("aabbccddeee")
print(f'{res} should be True')
res = sol.equalFrequency("aabbccdde")
print(f'{res} should be True')
res = sol.equalFrequency("abc")
print(f'{res} should be True')
res = sol.equalFrequency("abcdd")
print(f'{res} should be True')
res = sol.equalFrequency("abcddd")
print(f'{res} should be False')
res = sol.equalFrequency("aaabbbcccdd")
print(f'{res} should be False')      
