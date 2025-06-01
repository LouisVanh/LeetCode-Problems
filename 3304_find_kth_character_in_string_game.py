class Solution:
    string_list = ["a"]
    def kthCharacter(self, k: int) -> str:
        # print(self.string_list)
        if(len(self.string_list) > k):
            return self.string_list[k]
        
        def next_char(character):
            if(character == "z"):
                return "a"
            return chr(ord(character)+1)
        
        extra_chars = []
        for i in self.string_list:
            extra_chars.append(next_char(i))
        
        self.string_list.extend(extra_chars)
        return self.kthCharacter(k)
sol = Solution()
r=sol.kthCharacter(50)
print(r)