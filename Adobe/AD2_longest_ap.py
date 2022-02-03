import collections

class Solution:
    def lengthOfLongestAP(self, A, n):
        if n <= 2:  return n
        res = 1
        dp = [collections.defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                diff = A[i] - A[j]
                dp[i][diff] = max(dp[i][diff], 1 + dp[j][diff])
                res = max(res, dp[i][diff])
        return res + 1
