class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum =0
        if x%10 ==0 and x!=0: return False
        if x<0: return False
        while x>reversedNum:
            reversedNum = reversedNum*10 + x%10
            x = (int)(x/10)
        if (reversedNum == x) or ((int)(reversedNum/10) == x):return True
        else: return False


#https://leetcode.com/problems/palindrome-number/