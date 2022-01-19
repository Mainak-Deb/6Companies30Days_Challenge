class Solution{   
public:
    string printMinNumberForPattern(string str){
        stack<string> st;
        string ans = "";
        int num = 1;
        int n = str.size();
        for (int i = 0; i < n; i++){
        if (str[i] == 'D'){
            st.push(to_string(num));
            num++;
        }
        else{
            st.push(to_string(num));
            num++;

            while (st.size() > 0){
            ans += st.top();
            st.pop();
            }
        }
        }
        st.push(to_string(num));
        while (st.size() > 0){
        ans += st.top();
        st.pop();
        }
        return ans;
        }
};
