class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=sum(nums)
        for i,val in enumerate(nums):
            if a==(b-a-val):
                return i
            a+=val
        return -1
        