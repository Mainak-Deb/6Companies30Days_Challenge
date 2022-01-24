#User function Template for python3

class Solution:
    def colName (self, n):
        ans="";c=n
        while(c!=0):
            ans=chr(ord("A")+((c-1)%26))+ans
            c=(c-1)//26
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends