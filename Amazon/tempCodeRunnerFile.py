class Solution:
    def skipMdeleteN(self, head, M, N):
        node=head
        while((node!=None) and (M>1)):
            node=node.next
            M-=1
        p=node
        while((p!=None) and (N>1)):
            p=p.next
            N-=1
        node.next=p.next
