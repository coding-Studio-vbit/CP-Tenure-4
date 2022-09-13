class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        num = (''.join(map(str, digits)))
        num = str(int(num) + 1)
        return list(map(int, num))

x = Solution()
print((x.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3])))
print((x.plusOne([9,9,9])))

