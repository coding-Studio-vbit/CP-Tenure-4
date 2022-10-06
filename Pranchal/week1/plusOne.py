class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)-1
        while length>-1:
            if digits[length]<9:
                digits[length]=digits[length]+1
                return digits
            else:
                digits[length]=0
                length = length-1
                print(length>-1)
        digits.insert(0,'1')
        return digits


#https://leetcode.com/problems/plus-one/