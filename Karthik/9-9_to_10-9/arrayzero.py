
def minimumOperations(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    selected=minother(nums)
    count=0
    while(nums.count(0)!=len(nums)):
        subract=nums[selected]
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i]=nums[i]-subract
        if nums[selected]==0:
            selected=minother(nums)
        count+=1
    return count

def minother(nums):
    min=nums.index(max(nums))
    for i in range(len(nums)):
        if nums[i]!=0 and nums[i]<nums[min]:
            min=i
    return min

minimumOperations([1,5,0,3,5])
        