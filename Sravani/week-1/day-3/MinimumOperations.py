class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x != 0, nums))
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        nums.sort()
        m= nums[0]
        count = 0
        Flag = True 
        while(nums != [0]*len(nums)):
            nums = [x - m for x in nums]
            nums = list(filter(lambda x: x != 0, nums))
            if len(nums)!=0:
                m = min(nums)
            count +=1
          
        return count
        