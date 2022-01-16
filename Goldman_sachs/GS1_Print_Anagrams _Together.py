class Solution:
    def Anagrams(self, words, n):
        d={};ans=[]
        for i in words:
            a="".join(sorted(i))
            if a not in d.keys():d[a]=[i]
            else:d[a].append(i)
        for i in d.keys(): ans.append(d[i])
        return ans
