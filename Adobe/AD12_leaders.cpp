
class Solution{
    public:
    vector<int> leaders(int a[], int n){
        vector<int>ans;
        list<int>l;
        l.push_front(a[n-1]);
        for(int i=n-2;i>=0;i--){
            if(l.front()<=a[i]){
                l.push_front(a[i]);
            }
        }
        for(auto i:l){
            ans.push_back(i);
        }
        l.clear();
        return ans;
    }
};
