class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        if 0 in nums:
            return len(nums)-1
        else:
            return len(nums)
          
# second way
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
              count = 0
        n = len(nums)
        
        while nums != [0]*n:
            count+=1
            x = min([i for i in nums if i> 0])
            for i in range(n):
                if nums[i]!=0:
                    nums[i]-=x
        return count
      
# third way
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
      return len(set(x for x in nums if x > 0))
