vector<string> generate(int n)
{
	// Your code here
	vector<string> ans;
	int i, j, k;
	for (i = 1; i <= n; i++)
	{
		string temp = bitset<64>(i).to_string();
		const auto loc1 = temp.find('1');

		if (loc1 != string::npos)
			ans.push_back(temp.substr(loc1));
	}
	return ans;
}