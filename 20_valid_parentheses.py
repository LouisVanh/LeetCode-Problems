class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 != 0):
            return False
            
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if(i in pairs.keys()): # starting brace
                 stack.append(i)
            else: # ending brace
                # if the previous item was my opening brace, pop it
                if(stack == []): return False
                if(pairs[stack[len(stack)-1]] == i):
                    stack.pop()
                else:
                    return False
        
        return stack == []

so = Solution()
re = so.isValid("((){}[])")
print(re)

re = so.isValid("[{}]{((){}[]){}[]}")
print(re)

re = so.isValid("(((((((([{} ]{((){}[]){}[]})     )))))))")
print(re)

re = so.isValid(")(")
print(re)