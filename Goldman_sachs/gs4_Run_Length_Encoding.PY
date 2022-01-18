def encode(arr):
    ans=arr[0]
    count=1;l=len(arr)
    for i in range(l):
        if((i==l-1) or (arr[i]!=arr[i+1])):
            ans=ans+str(count)
            if(i!=l-1):
                ans=ans+arr[i+1]
            count=1
        else:count+=1
    return ans

