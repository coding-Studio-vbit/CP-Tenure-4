class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo,hi = i+1,len(nums)-1
            while lo < hi:
                tot = nums[i] + nums[lo] + nums[hi]
                if tot > 0:
                    hi -= 1
                elif tot < 0:
                    lo += 1
                else:
                    res.append([nums[i],nums[lo],nums[hi]])
                    lo += 1
                    while nums[lo] == nums[lo-1] and lo < hi:
                        lo += 1
        return res