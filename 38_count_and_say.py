class Solution:
    def countAndSay(self, n: int) -> str:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
        if(n == 1):
            return "1"
        return self.countAndSay(n-1)
    # quitting, can't do this yet.