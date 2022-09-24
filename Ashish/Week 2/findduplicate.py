class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        a = set()
        for i in range(n):
            if nums[i] in a:
                return nums[i]
            else:
                a.add(nums[i])