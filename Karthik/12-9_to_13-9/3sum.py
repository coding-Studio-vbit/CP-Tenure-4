class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets=[]
        for i,val in enumerate(nums[0:-2]):
            if val>0:
                break
            if val==nums[i-1] and i>0:
                continue
            left=i+1
            right=len(nums)-1
            while(left<right):
                sumof=nums[left]+val+nums[right]
                if sumof==0:
                    triplets.append([nums[left],val,nums[right]])
                if sumof>0:
                    right-=1
                else:
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return triplets
            