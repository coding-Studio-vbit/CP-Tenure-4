class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = len(nums)
        m = float(sum(nums[:k]))
        s = m
        for i in range(k, l):
            s = float(s + nums[i] - nums[i-k])
            m = max(m,s)
            
        return m/k
                        