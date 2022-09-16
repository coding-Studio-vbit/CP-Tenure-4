class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        tot = 0
        ans = float("inf")
        for r in range(len(nums)):
            tot+=nums[r]
            while tot>=target:
                ans = min(r-l+1, ans)
                tot-=nums[l]
                l+=1
                
        return 0 if ans == float("inf") else ans
        
