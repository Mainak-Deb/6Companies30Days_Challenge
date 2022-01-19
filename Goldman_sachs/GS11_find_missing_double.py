
class Solution:
    def findTwoElement( self,arr, n): 
       x=y=0
       for i in range(n):
           if(arr[abs(arr[i])-1]<0):x=abs(arr[i])
           else:arr[abs(arr[i])-1]=(-1*arr[abs(arr[i])-1])
       for i in range(n):
           if(arr[i]>0):y=i+1
       return [x,y]
           