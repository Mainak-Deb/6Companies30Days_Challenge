class Solution:
    grid=[]
    def valid(self,x,y):
        if ((0<=x<len(self.grid)) and (0<=y<len(self.grid[0]))):return True
        else:return False
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid=grid
        rottens=[]
        count=0;ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):rottens.append([i,j])
                if(grid[i][j]==1):count+=1
        rottens.append([])
        while(len(rottens)>0):
            if(len(rottens[0])==0):
                ans+=1
                if(len(rottens)>1):rottens.append([])
            else:
                x=rottens[0][0];y=rottens[0][1];
                if((self.valid(x+1,y)) and (grid[x+1][y]==1) ):
                    grid[x+1][y]=2;count-=1
                    rottens.append([x+1,y])
                if((self.valid(x,y+1)) and (grid[x][y+1]==1) ):
                    grid[x][y+1]=2;count-=1
                    rottens.append([x,y+1])
                if((self.valid(x-1,y)) and (grid[x-1][y]==1) ):
                    grid[x-1][y]=2;count-=1
                    rottens.append([x-1,y])
                if((self.valid(x,y-1)) and (grid[x][y-1]==1) ):
                    grid[x][y-1]=2;count-=1
                    rottens.append([x,y-1])
            rottens.pop(0)
        
        if(count>0):return -1
        else:return ans-1
        
        