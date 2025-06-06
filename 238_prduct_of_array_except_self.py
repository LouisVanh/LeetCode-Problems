class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach : suffix * prefix
        # make prefix list
        length = len(nums)
        prefixes, suffixes = [1], [1]*(length+1)
        for index in range(length):
            prefixes.append(nums[index] * prefixes[index])

        prefixes = prefixes[:-1]
        
        # make suffix list
        for index in range(length-1,-1,-1):
            # print(f"now calculating: {nums[index]} * {suffixes[index+1]}")
            suffixes[index] = nums[index] * suffixes[index+1]

        suffixes = suffixes[1:]
        
        
        # print(f"prefixes: {prefixes}" )
        # print(f"suffixes: {suffixes}" )
        output = []
        for i in range(length):
            output.append(prefixes[i]*suffixes[i])
        return output
