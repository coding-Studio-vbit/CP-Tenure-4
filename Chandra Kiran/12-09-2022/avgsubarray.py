from cmath import inf


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        max = -inf
        
        sum = 0

        for i in range(len(nums)):
            sum+=nums[i]

            if i>=k-1:
                avg = sum/k
                if avg>max:
                    max = avg
                sum-=nums[j]
                j+=1
        return max

            
