class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        i = len(digits)-1
        while (flag and i>=0):
            if digits[i]==9:
                digits[i] = 0
            else:
                digits[i] += 1
                flag = False
            i-=1
        if flag == True:
            digits.insert(0, 1)
        return digits