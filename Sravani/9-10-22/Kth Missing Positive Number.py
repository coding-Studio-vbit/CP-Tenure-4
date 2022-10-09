class Solution(object):
    def findKthPositive(self, arr, k):
        missing = []
        y = k+arr[-1]
        for i in range(1,y+1):
            if i not in arr:
                missing.append(i)
        return missing[k-1]
       