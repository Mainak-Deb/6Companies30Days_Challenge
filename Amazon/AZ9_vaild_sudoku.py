#User function Template for python3

class Solution:
    def isValid(self, mat):
        def check(x,y,arr):
            for i in range(len(arr)):
                if((arr[x][y]==arr[i][y]) and (i!=x)):return 0
                if((arr[x][y]==arr[x][i]) and (i!=y)):return 0
            startx=(x//3)*3
            starty=(y//3)*3
            for i in range(startx,startx+3):
                for j in range(starty,starty+3):
                    if((arr[i][j]==arr[x][y])  and( (i!=x) and (j!=y))):return 0
            return 1
                     
        
        for i in range(len(mat)):
         for j in range(len(mat[0])):
                if(mat[i][j]!=0):
                    b=check(i,j,mat)
                    if(not b):return 0
                    
                
        return 1;
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends