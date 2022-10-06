class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(s)
        if n == len(t):
            if s == t:
                return True
            else:
                return False
        a = 0
        for i in s:
            a = t.find(i,a)
            if a == -1:
                return False
        return True
        