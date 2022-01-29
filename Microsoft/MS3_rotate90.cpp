void rotate(vector<vector<int>>& matrix) {
        int n=matrix.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i<j){
                    swap( matrix.at(i).at(j),matrix.at(j).at(i));
                }
            }
        }
        for(int i=0;i<n/2;i++){
            for(int j=0;j<n;j++){
               swap( matrix.at(i).at(j),matrix.at(n-1-i).at(j));
            }
        }
        
    }