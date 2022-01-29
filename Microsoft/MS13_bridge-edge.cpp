
class Solution
{
public:
    int dfs(int i, vector<int> adj[], vector<int> &v, int c, int d)
    {
        v[i] = 1;
        for (auto x : adj[i])
        {
            if (i == c && x == d) continue;
            if (!v[x]) dfs(x, adj, v, c, d);
        }
        return 0;
    }

    int isBridge(int V, vector<int> adj[], int c, int d)
    {
        // Code here
        vector<int> v(100001);
        for (int i = 0; i < V; i++)
        {
            v[i] = 0;
        }

        dfs(c, adj, v, c, d);

        return (!v[d]);
    }
};
