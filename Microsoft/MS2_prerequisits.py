class Solution:
    def isPossible(self, N, prerequisites):
        def dfs(i):
            color[i] = 1
            if i in graph:
                for j in graph[i]:
                    if color[j] == 0:
                        if not dfs(j):
                            return False
                    elif color[j] == 1:
                        return False
            color[i] = 2
            return True
                            
        graph = {}
        for pair in prerequisites:
            if pair[1] in graph:
                graph[pair[1]].add(pair[0])
            else:
                graph[pair[1]] = set([pair[0]])			
        color = [0]*N
        for i in range(N):
            if color[i] == 0:
                if not dfs(i):
                    return False
        return True