class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ele = ''
        for i in digits:
            ele = ele + str(i)
        integer = int(ele)+1
        return list(str(integer))
        