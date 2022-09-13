class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k-1
        
        s = sum(nums[0:k])
        avg = s/k
        max_avg = avg
        
        i+=1
        j+=1
        while(j<len(nums)):
            s += nums[j] - nums[i-1]
            avg = s/k
            max_avg = max(avg, max_avg)
            i+=1
            j+=1
            
        return max_avg
            
            
        