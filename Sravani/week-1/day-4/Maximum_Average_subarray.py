class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxAvg=float("-inf")
        currAvg = 0 
        i=j=0 
        while j<n:
            currAvg +=nums[j] 
            if(j-i)+1 == k:
                maxAvg=max(maxAvg,currAvg/k)
                currAvg -=nums[i]
                i=i+1
            j +=1
        return maxAvg