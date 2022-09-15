class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lo,tot = 0,0
        res = len(nums)+1
        for i in range(len(nums)):
            tot += nums[i]
            while tot >= target:
                res = min(res,i-lo+1)
                tot -= nums[lo]
                lo += 1
        if res == len(nums)+1:
            return 0
        else:
            return res