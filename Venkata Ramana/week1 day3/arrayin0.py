class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = set()
        for i in nums:
            if i==0:
                continue
            if i in op:
                continue
            op.add(i)
        
        return len(op)
        