#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
            hash=[False]*26
            queue=[]
            ans=""
            for i in A:
                if(not hash[ord(i)-ord("a")]):
                    queue.append(i)
                    ans+=queue[0]
                    hash[ord(i)-ord("a")]=True
                else:
                    if(i in queue):queue.remove(i)
                    if(len(queue)==0):ans+="#"
                    else:ans+=queue[0]
            return ans
	            
		        
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends