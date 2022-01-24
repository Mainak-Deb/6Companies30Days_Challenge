
class Solution{
public:
    string matrixChainOrder(int p[], int n) {
        int matrix[100][100];
        int s[100][100];
        int i, j, k;
        for (i = 0; i < n ; i++){
            matrix[i][i] = 0;
        }

        int l;
        for (l = 2; l < n ; l++){
            for (i = 0; i < n - l + 1; i++){
                j = i + l - 1;
                matrix[i][j] = INT_MAX;
                for (k = i ; k < j ; k++){
                    int q = matrix[i][k] + matrix[k + 1][j] + p[i - 1] * p[j] * p[k];
                    if (q < matrix[i][j]){
                        matrix[i][j] = q;
                        s[i][j] = k;
                    }
                }
            }
        }
        char var = 'A';
        string ans;
        Brackets(1, n - 1, s, var, ans);
        return ans;
    }
    void Brackets(int i, int j, int s[100][100], char &var, string &ans){
        if (i == j){
            ans.push_back(var);
            var++;
            return;
        }

        ans.push_back('(');
        Brackets(i, s[i][j], s, var, ans);
        Brackets(s[i][j] + 1, j, s, var, ans);

        ans.push_back(')');
    }
};