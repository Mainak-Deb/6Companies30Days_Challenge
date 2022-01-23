#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        ans=[]
        contact=sorted(list(set(contact)))
        check=[True]*len(contact)
        for i in range(len(s)):
            a=[]
            for j in range(len(contact)):
                if((i<len(contact[j])) and (check[j])):
                    if(contact[j][i]==s[i]):
                        a.append(contact[j])
                    else:check[j]=False
                        
            if(len(a)):ans.append(a)
            else:ans.append([0])
            
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends