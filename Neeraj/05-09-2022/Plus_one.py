  class Solution:
    def plusOne(self, digits):
        if len(digits) == 0:
            return [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] +=1
