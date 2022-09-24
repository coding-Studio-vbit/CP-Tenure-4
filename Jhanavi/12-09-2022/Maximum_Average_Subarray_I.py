class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         window = max_sum = sum(nums[:k])
         for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            max_sum = max(max_sum, window)
         return max_sum / k
