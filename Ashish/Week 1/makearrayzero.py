class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num = set(nums)
        if(0 in num):
            return len(num) -1
        else:
            return len(num)