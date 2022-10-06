class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        lsum = 0
        rsum = sum(A)
        for i in range(0,len(A)):
            rsum -= A[i]
            if lsum == rsum:
                return i+1
            lsum += A[i]
        return -1
            