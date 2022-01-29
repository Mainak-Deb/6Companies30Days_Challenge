class Solution:
    def fourSum(self, arr, k):
        di={};ans=[]
        
        arr.sort()
        #print(arr)
        for i in range(len(arr)):di[arr[i]]=i
            
            
        for i in range((len(arr))):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    weneed=k-(arr[i]+arr[j]+arr[k])
                    if(weneed in di):
                        if(di[weneed]>k):
                            if([arr[i],arr[j],arr[k],weneed] not in ans):
                                ans.append([arr[i],arr[j],arr[k],weneed])

                       
        return ans
