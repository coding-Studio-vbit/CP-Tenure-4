class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        runningSum = 0
        shortest = maxsize
        
        left = 0
        
        for i, n  in enumerate(nums):
            runningSum = runningSum + n
            
            # try compressing maximally
            while runningSum >= target:
                shortest = min(shortest, (i - left) + 1)
                runningSum = runningSum - nums[left]
                left = left + 1
                
        if shortest == maxsize:
            return 0
        else:
            return shortest