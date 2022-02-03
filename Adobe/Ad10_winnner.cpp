class Solution{
  public:
  
    //Function to return the name of candidate that received maximum votes.
    vector<string> winner(string arr[],int n)
    {
        unordered_map<string,int>mp;
        for(int i=0;i<n;i++){
            mp[arr[i]]++;
        }
        int maxi=mp[arr[0]];
        string name=arr[0];
        for(int i=1;i<n;i++){
            if(mp[arr[i]]>maxi){
                maxi=mp[arr[i]];
                name=arr[i];
            }else if(mp[arr[i]]==maxi){
                if(name>arr[i]){
                    name=arr[i];
                }
            }
        }
        vector<string>ans;
        ans.push_back(name);
        ans.push_back(to_string(maxi));
        return ans;
       
    }
};
