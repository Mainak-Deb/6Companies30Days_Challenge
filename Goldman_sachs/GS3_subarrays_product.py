
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        mul=1;ans=0;l=n
        right=0;left=0
        while(right<l):
            mul*=a[right]
            while((left<l) and (mul>=k)):
                mul=mul/a[left]
                left+=1
            if(mul<k):ans+=(right-left+1)
            right+=1
        return ans
 