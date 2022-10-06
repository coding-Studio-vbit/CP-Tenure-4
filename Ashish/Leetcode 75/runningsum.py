class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = []
        n = len(nums)
        for i in range(n):
            if not runningsum:
                runningsum.append(nums[i])
            else:
                runningsum.append(runningsum[-1]+nums[i])
        return runningsum