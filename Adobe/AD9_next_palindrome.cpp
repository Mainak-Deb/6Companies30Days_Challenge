class Solution{
  public:
    string nextPalin(string N) { 
        //complete the function here
        if(N.length()<=3){
            return "-1";
        }
        int midIndx = N.size()/2;
        //cout<<midIndx<< " "<<N[midIndx]<<endl;
        string prev = N.substr(0,midIndx);
        int len = prev.length();
        int ind = len;
        for(int i=len-1;i>0;i--){
            if(prev[i]>prev[i-1]){
                ind=i-1;
                break;
            }
        }
        if(ind==len){
            return "-1";
        }
        for(int i=len-1;i>0;i--){
            if(prev[i]>prev[ind]){
                swap(prev[i],prev[ind]);
                break;
            }
        }
        sort(prev.begin()+ind+1,prev.end());
        string ans="";
        ans+=prev;
        if(N.size()%2!=0){
            ans+=N[N.size()/2];
        }
        reverse(prev.begin(),prev.end());
        ans+=prev;
        return ans;
    }
};