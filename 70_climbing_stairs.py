class Solution:
    global lookup_table
    lookup_table = [0,1,2,3,5,8]
    def climbStairs(self, n: int) -> int:
        if(n <= 3): return n
        if(len(lookup_table) > n):
            print(f"found in lookup_table with length {len(lookup_table)}: {n}")
            return lookup_table[n]
        else:
            if(n == len(lookup_table)):
                print("please append")
                print(lookup_table)
                lookup_table.append(lookup_table[-1] + lookup_table[-2])
                print(lookup_table)

            return self.climbStairs( n-1) + self.climbStairs(n-2)
        
sol = Solution()
print(sol.climbStairs(40))