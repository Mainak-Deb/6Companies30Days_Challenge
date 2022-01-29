
class Solution{

  public:
	int minDifference(int a[], int n)  {
        int sm = 0;
        int i , j, k;
        for (int i = 0; i < n ; i++)
        {
            sm += a[i];
        }
        int answer = divadd(a, n, sm);
        return answer;
    }
    int divadd(int a[] , int n , int m)
    {
        bool dp[n + 1][m + 1];

        int i, j, k;
        for (i = 0; i <= m; i++)
        {
            dp[0][i] = false;
        }
        for (i = 0; i <= n; i++)
        {
            dp[i][0] = true;
        }
        for (i = 1; i <= n; i++)
        {
            for (j = 1; j <= m; j++)
            {
                if (a[i - 1] <= j) 
                {
                    dp[i][j] = dp[i - 1][j - a[i - 1]] || dp[i - 1][j];
                }
                else 
                {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
     
        vector<int> vec;
        for (i = 0; i <= m / 2; i++) 
        {
            if (dp[n][i] == true)
            {
                vec.push_back(i);
            }
        }
        int mn = INT_MAX;
        for (i = 0; i < vec.size(); i++)
        {
            mn = min(mn, m - (2 * vec[i]));
        }
        return mn; 
    }

    
};
