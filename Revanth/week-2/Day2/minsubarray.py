class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, s = 0,0
        out = float("inf")
        for i in range(len(nums)):
            s +=nums[i]
            while s >= target:
                out = min(i - l + 1, out)
                s -= nums[l]
                l += 1
        return 0 if out == float("inf") else out
                
