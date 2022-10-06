class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0,len(nums)
        while True:
            mid = int((l+h)/2)
            if l > h:
                return -1
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                h = mid