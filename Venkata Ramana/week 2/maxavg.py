class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cur = ans = sum(nums[:k])
        for i, num in enumerate(nums[k:]):
            cur = cur - nums[i] + num
            ans = max(cur, ans)
        return ans * 1.0 / k
        