def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        true_x = x
        rev = 0
        while x:
            rev = (rev*10) + (x%10)
            x = x//10
        if true_x == rev:
            return True
        else:
            return False