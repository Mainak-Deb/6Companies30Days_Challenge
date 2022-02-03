class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        nonneg=s.strip()
        if(nonneg[0]=='-1'):nonneg=nonneg[1:]
        if(not s.isdigit()):return -1
        neg=1
        c=""
        flag=0
        for i in s:
            if i==' ':
                if flag>0:
                    break
                continue
            elif i.isalpha():
                flag+=1
                break
            elif i=='+':
                flag+=1
                if flag>=2:
                    break
            elif i=='-':
                flag+=1
                if flag>=2:
                    break
                neg=-1
            else:
                flag+=1
                c+=i
        if c=="":
            return 0
        res=int(float(c))
        if -2**(31)>res*neg:
            return -2**(31)
        if 2**(31)-1<res*neg:
            return 2**(31)-1
        return res*neg
