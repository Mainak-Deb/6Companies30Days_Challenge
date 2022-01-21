class Solution:
    def maxProfit(self, K,N, A):
        if((K<1) or (N<1)):return 0
        arr=[[0]*N for i in range(K+1)]
        for i in range(1,K+1):
            mx=arr[i-1][0]-A[0]
            for j in range(1,N):
                arr[i][j]=max(arr[i][j-1],A[j]+mx)
                if(arr[i-1][j]-A[j]>mx):mx=arr[i-1][j]-A[j]
        return arr[-1][-1]
        