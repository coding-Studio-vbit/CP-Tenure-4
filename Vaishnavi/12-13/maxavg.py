class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum,curr_sum = 0,0
        for i in range(k):
            sum += nums[i]
        curr_sum = sum
        for i in range(k,len(nums)):
            curr_sum += nums[i]-nums[i-k]
            sum = max(sum,curr_sum)
        return sum/k