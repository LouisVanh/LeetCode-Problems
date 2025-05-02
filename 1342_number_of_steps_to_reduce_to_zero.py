class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num !=0:
            # print(f"{num} is num and counter is {counter}")
            if(num%2==0):
                num=num>>1
            else:
                num-=1
            
            counter+=1

        return counter

sol = Solution()
r=sol.numberOfSteps(15)
print(r)