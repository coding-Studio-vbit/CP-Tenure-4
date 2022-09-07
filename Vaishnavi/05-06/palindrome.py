def isPalindrome(self, x: int) -> bool:
        res = False
        x = str(x)
        n = len(x)
        if n == 1:
            res = True
        for i in range(n//2):
            if x[i] == x[n-1-i]:
                res = True
            else:
                res = False
                break
        return res