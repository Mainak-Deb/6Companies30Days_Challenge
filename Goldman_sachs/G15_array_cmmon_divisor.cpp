class Solution {
  public:
    bool canPair(vector<int> nums, int k) {
        if (nums.size() % 2 != 0) 
                return false;

        int i, j;
        int n = nums.size();

        unordered_map<int, int> hsh;
        for (i = 0; i < n; i++)
        {
            hsh[nums[i] % k]++;
        }
        for (i = 0; i < n; i++)
        {
            int extra = nums[i] % k;

            if (extra == 0)
            {
                if (hsh[extra] % 2 != 0)
                {
                    return false;
                }
            }
            else if (2 * extra == k)
            {
                if (hsh[extra] % 2 != 0)
                {
                    return false;
                }
            }
            else
            {
                if (hsh[extra] != hsh[k - extra]) return false;
            }
        }
        return true;
    };
}