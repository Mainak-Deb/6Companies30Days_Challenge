class Solution:
    def findPosition(self, N , M , K):
        return ((M+K-1)%N) if ((M+K-1)%N) else N
