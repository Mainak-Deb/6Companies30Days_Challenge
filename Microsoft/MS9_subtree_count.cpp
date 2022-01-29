
int solve(Node* root, int x, int &ans)
{
    if (root == NULL)
    {
        return 0;
    }

    int ls = solve(root->left, x, ans);
    int rs = solve(root->right, x, ans);

    int sum = root->data + ls + rs;
    if (sum == x) ans++;
    return sum;
}

int countSubtreesWithSumX(Node* root, int x)
{
    // Code here
    int ans = 0;
    solve(root, x, ans);
    return ans;
}
