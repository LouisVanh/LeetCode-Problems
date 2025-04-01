import sympy
import math
class Solution:
    def isThree(self, n: int) -> bool:
        if(n<4):
            return False
        # The only numbers with three divisors are squares of prime numbers (itself, 1, and the prime)
        primes = list(sympy.primerange(1, 1000))
        if(math.sqrt(n) in primes):
            return True
        
        else: return False