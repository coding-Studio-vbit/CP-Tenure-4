class Solution(object):
    def groupAnagrams(self, strs):
        from collections import Counter
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedstr={}
        for i in strs:
            value=''.join(sorted(i))
            if value in sortedstr:
                sortedstr[value].append(i)
            else:
                sortedstr[value]=[i]
        return list(sortedstr.values())