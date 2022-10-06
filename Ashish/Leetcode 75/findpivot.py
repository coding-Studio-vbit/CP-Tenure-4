class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sl,sr = 0,0
        for i in range(n):
            if sl == 0 and sr == 0:
                sl = sum(nums[0:i])
                sr = sum(nums[i+1:n])
                if(sl == sr):
                    return i
            else:
                sl = sl + nums[i-1]
                sr = sr - nums[i]
                if(sl == sr):
                    return i
        return -1