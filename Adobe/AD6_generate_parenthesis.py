class Solution:
    ans=set()
    def make(self,par,r,l,sk):
        if not (l or r or sk):self.ans.add(par)
        if(l>0):self.make(par+"(",r,l-1,sk+1)
        if((sk>0) and (r>0)):self.make(par+")",r-1,l,sk-1)
    def AllParenthesis(self,n):
       self.ans=set()
       self.make("",n,n,0)
       return list(self.ans)
