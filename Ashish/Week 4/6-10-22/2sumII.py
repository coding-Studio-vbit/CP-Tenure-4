class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                a = [i+1,j+1]
                return a
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1