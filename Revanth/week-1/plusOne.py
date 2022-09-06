#plusOne

class Solution(object):
    def plusOne(self, digits):
        l = len(digits) - 1
        while l > -1:
            if digits[l] < 9:
                digits[l] += 1
                return digits
            else:
                digits[l] = 0
                l -= 1
        return [1] + digits 