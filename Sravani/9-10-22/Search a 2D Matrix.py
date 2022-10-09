class Solution(object):
    def searchMatrix(self, matrix, target):
        nums = [j for sub in matrix for j in sub]
       
        low = 0
        high=len(nums)-1
        mid= 0
        output = 0
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] <target:
                low = mid + 1
            elif nums[mid] >target:
                high = mid - 1
            else:
                output = True
                break
                
        if(output):
            return True
        else:
            return False