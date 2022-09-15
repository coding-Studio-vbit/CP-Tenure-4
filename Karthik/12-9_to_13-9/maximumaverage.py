
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumof=0.000
        a=0
        for i in range(len(nums)):
            sumof+=nums[i]
            if i>=k-1:
                if a==0:
                    max_sum=sumof
                max_sum=max(max_sum,sumof)
                sumof-=nums[i-(k-1)]
                a+=1
                
        return max_sum/k
        