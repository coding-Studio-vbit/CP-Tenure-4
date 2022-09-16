class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        arraymax=0
        while i<j:
            minimum=min(height[i],height[j])
            if minimum*(j-i)>arraymax:
                arraymax=minimum*(j-i)
            if minimum==height[i]:
                i+=1
            else:
                j-=1
        return arraymax
        
            
        