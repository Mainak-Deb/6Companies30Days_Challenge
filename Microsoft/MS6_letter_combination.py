class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        d={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9 :["w","x","y","z"],     
        }
        if(len(a)==0):return []
        ans=[i for i in d[a[0]]]

        if(len(a)>1):
            x=1
            while(x<len(a)):                
                for i in d[a[x]]:ans.append(ans[0]+i)
                ans.pop(0)
                if(len(ans[0])>x):x+=1

        return ans
        
        
