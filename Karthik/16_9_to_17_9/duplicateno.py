class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # setnums=set(nums)
        # maximum=0
        # maxnumber=0
        # for i in setnums:
        #     count=nums.count(i)
        #     if count>maximum:
        #         maximum=count
        #         maxnumber=i
        # return maxnumber
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                return nums[i]
        