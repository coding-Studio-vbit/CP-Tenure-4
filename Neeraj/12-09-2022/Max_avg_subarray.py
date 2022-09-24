class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        res = maxSum
        for i in range(k,len(nums)):
            maxSum+= nums[i]-nums[i-k]
            res = max(res,maxSum)
            
        return res/k
