class Solution {
	public:
    int mod=mod;
		int CountWays(string s){
		   int n = s.size();
    if (s[0] == '0') 
        return 0;
    for (int i = 0; i < n - 1; i++)
    {
      if (s[i] == '0' && s[i + 1] == '0') return 0;
    }
    if (s.size() == 1) return 1;

    int dp[n];
    dp[0] = 1;
    int i, j, k;
    for (i = 1; i < n; i++)
    {
      if (s[i] == '0' && s[i - 1] == '0')
      {
        dp[i] = 0;
      }
      else if (s[i - 1] == '0' && s[i] != '0')
      {
        dp[i] = dp[i - 1] % mod;
      }
      else if (s[i - 1] != '0' && s[i] == '0')
      {
        if (s[i - 1] == '1' || s[i - 1] == '2')
        {
          dp[i] = (i >= 2 ? dp[i - 2] % mod : 1) % mod;
        }
        else
        {
          dp[i] = 0;
        }
      }
      else
      {
        dp[i] = dp[i - 1] % mod;
        if (stoi(s.substr(i - 1, 2)) <= 26)
        {
          dp[i] += (i >= 2 ? dp[i - 2] % mod : 1) % mod;
        }
      }
    }
    return dp[n - 1] % mod;

		}

};
