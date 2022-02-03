class Solution:
	def numOfWays(self, n, x):
        dp=[0 for i in range(n+1)];
        dp[0]=1;
        dp[1]=1;
        r=int(n**(1/x))
        for i in range(2,r):
            for j in range(n,(i**x)-1,-1):dp[j]=dp[j]+dp[j-(i**x)];
        return dp[n]
               