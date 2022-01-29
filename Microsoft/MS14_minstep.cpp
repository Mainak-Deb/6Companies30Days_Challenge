class Solution {
public:
    int minSteps(int D) {
        int ans = 0,s = 0;
        while (1){
            s += ans;ans += 1;
            if (s == D) return ans - 1;     
            if (s > D && (s - D) % 2 == 0) return ans - 1;
        }return 0;
        
    }
};
