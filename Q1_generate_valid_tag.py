class Solution:
    def generateTag(self, caption: str) -> str:
        res = ''
        words = caption.split()
        word_count = 0
        for word in words:
            word_count+=1
            if(word_count == 1):
                res+=word.lower()
                continue
            res += word.capitalize()
            print(res)

        # Remove all non english chars
        new_res = "#"
        for char in res:
            if(char.isalpha()):
               new_res += char 
                
        
        return new_res[:100]