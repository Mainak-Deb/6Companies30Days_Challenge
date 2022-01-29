class Solution
{
public:
    int FindMaxSum(int nums[], int n)
    {

        if (n == 1)
        {
            return nums[0];
        }
        else if (n == 2)
        {
            return max(nums[0], nums[1]);
        }
        int i, j, k;
        int arr[n];
        arr[0] = nums[0];
        arr[1] = nums[1];
        arr[2] = nums[0] + nums[2];
        for (i = 3; i < n; i++)
        {
            arr[i] = nums[i] + max(arr[i - 3], arr[i - 2]);
        }
        int ans = INT_MIN;
        for (i = 0; i < n; i++)
        {
            ans = max(ans, arr[i]);
        }
        return ans;
    }
};
