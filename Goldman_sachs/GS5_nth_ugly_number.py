class Solution:
    def getNthUglyNo(self,n):
        ans=[1]
        v2=2;v3=3;v5=5
        p2=0;p3=0;p5=0
        for i in range(n):
                ans.append(min(v2,v3,v5))
                if(ans[-1]==v2):
                    p2+=1;v2=ans[p2]*2
                if(ans[-1]==v3):
                    p3+=1;v3=ans[p3]*3
                if(ans[-1]==v5):
                    p5+=1;v5=ans[p5]*5
        return ans[n-1]
                    