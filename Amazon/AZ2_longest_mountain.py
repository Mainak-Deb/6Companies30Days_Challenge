class Solution:
       
    def longestMountain(self, arr: List[int]) -> int:
        mx=0;up=0;down=0
        for i in range(len(arr)-1):
            if((down and (arr[i]<arr[i+1])) or (arr[i]==arr[i+1])):
                up=0;down=0
            if(arr[i]<arr[i+1]):up+=1
            if(arr[i]>arr[i+1]):down+=1
            if(up and down):mx=max(mx,up+down+1)
        return mx