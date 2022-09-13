class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        y=x
        if x<0 :
            return "false"
        while(x!=0):
            n=x%10
            rev=rev*10+n
            x=x//10
        if rev==y:
            return "true"
        return "false"