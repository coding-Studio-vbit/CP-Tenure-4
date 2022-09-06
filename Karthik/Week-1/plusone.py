class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numbers=""
        for i in digits:
            numbers+=str(i)
        intnum=int(numbers)+1
        finallist=[int(i) for i in str(intnum)]
        return finallist
        