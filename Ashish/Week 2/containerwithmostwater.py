class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height) - 1
        max1 = 0
        while i<j:
            h = min(height[i],height[j])
            l = j - i
            if(max1 <= h*l):
                max1 = h*l
            if(height[i] < height[j]):
                i+=1
            else:
                j-=1
        return max1