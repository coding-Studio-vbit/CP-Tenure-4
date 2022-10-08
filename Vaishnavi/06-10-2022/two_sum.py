class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        ans = []
        while l<r:
            if numbers[l] + numbers[r] == target:
                ans.append(l+1)
                ans.append(r+1)
                return ans
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1