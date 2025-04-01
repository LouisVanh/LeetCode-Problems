class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longest = str1 if len(str1) >= len(str2) else str2
        shortest = str1 if len(str1) < len(str2) else str2
        for shortest_length in range(len(shortest), 0, -1):
            if(len(shortest) % shortest_length or len(longest) % shortest_length):
                continue
            base = shortest[:shortest_length]
            amount_of_times_base_fits_in_longest = len(longest) // len(base)
            amount_of_times_base_fits_in_shortest = len(shortest) // len(base)
            print(f"s={amount_of_times_base_fits_in_shortest}, l = {amount_of_times_base_fits_in_longest} - B={base}")
            if longest == base*amount_of_times_base_fits_in_longest and shortest == base*amount_of_times_base_fits_in_shortest:
                return shortest[:shortest_length]
        return ""

sol = Solution()
r=sol.gcdOfStrings("LEET", "CODE")
print(r)
r=sol.gcdOfStrings("ABDABD", "ABD")
print(r)