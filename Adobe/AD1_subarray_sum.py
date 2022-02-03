class Solution:
    def subArraySum(self,arr, n, k): 
        s=0;e=1;sums=arr[0];ans=[];
        while(e<len(arr)):
           if(sums>k):
               sums-=arr[s];s+=1
           if(sums<k):
               sums+=arr[e];e+=1
           if(sums==k):return [s+1,e]
        return [-1]
       
    