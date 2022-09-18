class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxi = 0
        while (left<right):
            h1 = height[left]
            h2 = height[right]
            mini = min(h1,h2)
            maxi = max(maxi,mini*(right-left))
            if h1<h2:
                left += 1
            else:
                right -= 1
        return maxi