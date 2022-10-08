class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
                output = mid
                return output
    
        if output == False:
            for i in range(0,len(nums)):
                if target< min(nums):
                    return 0
                    break
                elif target> max(nums):
                    return len(nums)
                    break    
                elif nums[i]< target < nums[i+1]:
                    return i+1
                    break