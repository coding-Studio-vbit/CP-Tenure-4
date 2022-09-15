class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(set(nums))
        if 0 in set(nums):
            return l-1
        else:
            return l
