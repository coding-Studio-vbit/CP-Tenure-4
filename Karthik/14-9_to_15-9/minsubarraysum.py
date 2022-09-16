class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        sumof=0
        minimum=1e9
        for j in range(len(nums)):
            sumof+=nums[j]
            while sumof>=target:
                minimum=min(minimum,j-i+1)
                sumof-=nums[i]
                i+=1
        if minimum==1e9:
            return 0
        return minimum
                    
        