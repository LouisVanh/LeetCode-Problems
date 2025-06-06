from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + '#' + word
        print(res)
        return res
            
    def decode(self, s: str) -> List[str]:
        if s == "0#": return [""]
        
        res = []
        length_str = ""          # build the number as a string
        reading_word = False
        remaining = 0            # how many characters to read
        word = []

        for char in s:
            print('now doing char:' + str(char))

            if reading_word:
                print(f"adding char: {char} to word with remaining: {remaining}(READING)")
                word.append(char)
                remaining -= 1

                if remaining == 0:
                    reading_word = False
                    res.append("".join(word))
                    word = []
                    length_str = ""   # reset for next word

            else:
                if char != '#':
                    length_str += char
                else:
                    remaining = int(length_str)  # transfer to int here
                    if(remaining == 0):
                        reading_word = False
                        res.append("")
                    else: reading_word = True

        return res

