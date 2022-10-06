class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        game=[0.0]*(N+W+1)
        for k in range(K,N+1):
            game[k]=1.0
        Sum=min(N-K+1,W)
        for k in xrange(K-1,-1,-1):
            game[k]=Sum/float(W)
            Sum+=game[k]-game[k+W]
        return game[0]
        