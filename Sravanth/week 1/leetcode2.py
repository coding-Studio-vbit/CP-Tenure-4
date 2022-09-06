class Solution:
    def plusOne(self, digits: List[int]):
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])
        num1 = int(num)+1
        num = str(num1)
        for j in range(len(digits)):
            digits.remove(digits[0])
        for k in num:
            digits.append(k)
        return digits
