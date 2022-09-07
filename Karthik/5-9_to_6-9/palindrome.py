class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=0
        temp=x
        while(x>0):
            r=x%10
            s=s*10+r
            x//=10
        print(s)
        if s==temp:
            return True
        else:
            return False