class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        output = []
        while(True):
            if numbers[i]+numbers[j]==target:
                output.append(i+1)
                output.append(j+1)
                return output
               
            elif numbers[i]+numbers[j]<target:
                i+=1
                
            elif numbers[i]+numbers[j]>target:
                j-=1