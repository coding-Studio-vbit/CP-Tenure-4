class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<=10:
            return []
        d = {}
        l = []
        for i in range(10,len(s)+1):
            if s[i-10:i] not in d:
                d[s[i-10:i]]=1
            else:
                if d[s[i-10:i]]:
                    l.append(s[i-10:i])
                    d[s[i-10:i]] = 0 
        return l
