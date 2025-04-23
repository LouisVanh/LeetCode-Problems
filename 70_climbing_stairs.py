class Solution:
    #Recursion:
    # global lookup_table
    # lookup_table = [0,1,2,3,5,8]
    # def climbStairs(self, n: int) -> int:
    #     if(n <= 3): return n
    #     if(len(lookup_table) > n):
    #         print(f"found in lookup_table with length {len(lookup_table)}: {n}")
    #         return lookup_table[n]
    #     else:
    #         if(n == len(lookup_table)):
    #             print("please append")
    #             print(lookup_table)
    #             lookup_table.append(lookup_table[-1] + lookup_table[-2])
    #             print(lookup_table)

    #         return self.climbStairs( n-1) + self.climbStairs(n-2)


    # Bottoms up DP
    # def climbStairs(self, n: int) -> int:
    #     dp=[-1]*(n+1)
    #     dp[0] = 1
    #     dp[1] = 1

    #     for i in range(2,n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     print(dp)
    #     return dp[n]

    # DP: space optimised bottoms up
    # def climbStairs(self, n: int) -> int:
    #     if(n<=1): return 1
    #     prev2 = 1
    #     prev = 1
    #     curr = 1

    #     for _ in range(2,n+1):
    #         # tmp = prev2
    #         prev2 = prev
    #         prev = curr
    #         curr = prev+prev2
    #         print(curr, " is the curr value")
    #     return curr
    
    # recursive + hashmap memoization
    def climbStairs(self, n:int) -> int:
        cache = {}
        def recursive_memoization(n):
            if(n<=3): return n
            if(n in cache): return cache[n]

            else:
                result = recursive_memoization(n-2) + recursive_memoization(n-1)
                cache[n] = result
                return result
        
        return recursive_memoization(n)

sol = Solution()
print(sol.climbStairs(40))
print(sol.climbStairs(1))
print(sol.climbStairs(2))