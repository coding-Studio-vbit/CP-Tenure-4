class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = 0
        for i in range(k):
            sum1 += nums[i]
        res = sum1
        n = len(nums)
        for i in range(k,n):
            sum1 += nums[i] - nums[i-k]
            res = max(res,sum1)
        return res/k