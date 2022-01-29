class Solution
{
public:
	vector <int> calculateSpan(int price[], int n)
	{
		int i, j, k;
		stack<pair<int, int>> st;
		vector<int> v;
		st.push({price[0], 1});
		v.push_back(1);
		for (i = 1; i < n; i++)
		{
			int c = 1;
			while (!st.empty() && (st.top().first <= price[i]))
			{
				c += st.top().second;
				st.pop();
			}
			v.push_back(c);
			st.push({price[i] , c});
		}
		return v;
	}
};

