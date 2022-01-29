class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        ans=[]
        rowchk=[1 for i in range(len(matrix))]
        colchk=[1 for i in range(len(matrix[0]))]
        
        
        def spiral(arr,s,e,dirc):
            try:
                if( rowchk[s[1]] and rowchk[e[1]] and colchk[s[0]] and colchk[e[0]] ):
                    if(dirc=="r"):
                        for i in range(s[0],e[0]+1):ans.append(arr[s[1]][i])
                        rowchk[s[1]]=0;s[1]+=1
                        spiral(arr,s,e,"d")
                    elif(dirc=="d"):
                        for i in range(s[1],e[1]+1):ans.append(arr[i][e[0]])
                        colchk[e[0]]=0;e[0]-=1;
                        spiral(arr,s,e,"l")
                    elif(dirc=="l"):
                        for i in range(e[0],s[0]-1,-1):ans.append(arr[e[1]][i])
                        rowchk[e[1]]=0;e[1]-=1;
                        spiral(arr,s,e,"u")
                    elif(dirc=="u"):
                        for i in range(e[1],s[1]-1,-1):ans.append(arr[i][s[0]])
                        colchk[s[0]]=0;s[0]+=1
                        spiral(arr,s,e,"r")
            except:return
        spiral(matrix,[0,0],[len(matrix[0])-1,len(matrix)-1],"r")
        return ans;            
         
        
        