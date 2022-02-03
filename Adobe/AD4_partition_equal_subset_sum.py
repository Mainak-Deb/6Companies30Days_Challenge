class Solution:
    def equalPartition(self, N, arr):
        s = sum(arr)
        if s%2 == 1:return False			
        x = s // 2;b = 1		
        for i in arr:b = b | b<<i		
        return (b>>x) & 1 == 1 
