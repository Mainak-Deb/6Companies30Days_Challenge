
class Solution:
    def doOverlap(self, L1, R1, L2, R2):
        x1=abs(R1[0]-L1[0])
        y1=abs(R1[1]-L1[1])
        x2=abs(R2[0]-L2[0])
        y2=abs(R2[1]-L2[1])
        if(((-1*x2)<=(L2[0]-L1[0])<=x1) and ((-1*y2)<=(R2[1]-R1[1])<=y1) ):return 1
        return 0