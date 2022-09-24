class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        i,j = 0,0
        sum = 0    
        while(j < len(nums)):
            sum += nums[j]
            while(sum >= target):
                length = min(length, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        return 0 if length == float('inf') else length