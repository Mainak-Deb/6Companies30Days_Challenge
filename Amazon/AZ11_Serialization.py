# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    arr=[]
    def maxDepth(self,node):
        if node is None:return -1 ;
        else :
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)
            if (lDepth > rDepth):return lDepth+1
            else:return rDepth+1
    
    def dfs(self,root,i):
        if(root==None):return
        else:
            self.arr[i]=root.val
            self.dfs(root.left,(2*i)+1)
            self.dfs(root.right,(2*i)+2)
    
    def decode(self,arr,i):
        if(i<len(arr)):
            if(arr[i]=="None"):return None
            else:
                node=TreeNode(int(arr[i]))
                node.left=self.decode(arr,(2*i)+1)
                node.right=self.decode(arr,(2*i)+2)
                return node
    
    def serialize(self, root):
        if(root==None):return "None"
        h=self.maxDepth(root)
        self.arr=[None]*int((2**(h+1))-1)
        self.dfs(root,0)
        return ','.join(map(str, self.arr))
            

    def deserialize(self, data):                
        array=list(data.split(','))
        return self.decode(array,0)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))