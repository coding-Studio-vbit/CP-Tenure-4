class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for l in range(len(s)-9):
            if s[l:l+10] in seen:
                res.add(s[l:l+10])
            else:
                seen.add(s[l:l+10])
        return res
