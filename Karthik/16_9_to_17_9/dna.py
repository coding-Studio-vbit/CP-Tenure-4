class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output=[]
        if len(s)>10:
            if len(set(s))==1:
                output.append(s[0:10])
            else:
                b=set()
                for i in range(len(s)-10+1):
                    substr=s[i:i+10]
                    # if s.count(b[i])>=2:
                    #     if b[i] not in output:
                    #         output.append(b[i])
                    # else:
                    #     if i==1:
                    #         if b[i].count():
                    #             output.append(b[i])
                    # print(b[i])
                    if substr in b and substr not in output:
                        output.append(substr)
                    else:
                        b.add(substr)
                
        else:
            output=[]
        return output