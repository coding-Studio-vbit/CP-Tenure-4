class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == [0]*n:
            return 0
        count = 0
        while True:
            nums.sort()
            if 0 in nums:
                z_count = nums.count(0)
                nums = nums[z_count:]
            if nums == []:
                return count
            mini = nums[0]
            for i in range(len(nums)):
                nums[i] -= mini
            count += 1