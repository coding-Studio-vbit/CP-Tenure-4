class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0, len(numbers)-1
        arr = []
        
        while(True):
            if numbers[i]+numbers[j] == target:
                arr.append(i+1)
                arr.append(j+1)
                return arr 
            elif numbers[i] + numbers[j] > target:
                j -=1
            elif numbers[i] + numbers[j] < target:
                i +=1
        