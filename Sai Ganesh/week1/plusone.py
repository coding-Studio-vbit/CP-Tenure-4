class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        for i in digits:
            sum=sum*10+i
        sum=sum+1
        ls=[]
        for i in range(len(str(sum))):
            ele=sum%10
            ls.append(ele)
            sum=sum//10
        ls=ls[::-1]
        return ls