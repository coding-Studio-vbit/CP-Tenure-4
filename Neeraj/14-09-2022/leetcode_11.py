class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height)-1
        
        while l<r:
            if height[l]<height[r]:
                res = height[l]*(r-l)
                l+=1
            else:
                res = height[r]*(r-l)
                r-=1
            ans = max(ans, res)
                
                
        return ans
