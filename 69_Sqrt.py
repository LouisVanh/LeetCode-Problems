class Solution:
    def mySqrt(self, x: int) -> int:
        # Imagine a massive list from 0- infinity
        # Our sqrt is definitely going to be between 0 and x
        # check the half of it, try it out.
        # Let's say we're given 101, try 50
        # Didn't work, shucks, try 25
        # Didn't work, shucks, try 12
        # Didn't work, shucks, try 6
        # Wait... we're now lower than it. It must be between 6 and 12. Try (12-6)//2 + 6 = 9 
        # Wait... we're now lower than it. It must be between 9 and 12. Try (12-9)//2 + 9 = 10
        # Wait... we're now lower than it. It must be between 10 and 12. Try (12-10)//2 + 10 = 11
        # Wait... we're now higher than it. It must be between 10 and 11. As the difference between left and right is <= 1, return the left value
        # If we're given a number that has a sqrt, simply keep running until we find the value

        left, right, mid = 0, x, x//2
        if(x == 1):
            return 1
        while True:
            # Success, number found
            sqr = mid*mid
            if(sqr == x):
                return mid
            
            elif(right-left <= 1):
                return left
            
            elif(sqr < x):
                print(f"{mid} is smaller than sqrt(x)")
                left = mid
                mid = (right-left)//2 + left

            elif(sqr > x):
                print(f"{mid} is bigger than sqrt(x)")
                right = mid
                mid = (right-left)//2 + left

sol = Solution()
r = sol.mySqrt(101)
print(r)
r = sol.mySqrt(1)
print(r)
r = sol.mySqrt(2)
print(r)
r = sol.mySqrt(4)
print(r)
r = sol.mySqrt(0)
print(r)
r = sol.mySqrt(403992423)
print(r)
