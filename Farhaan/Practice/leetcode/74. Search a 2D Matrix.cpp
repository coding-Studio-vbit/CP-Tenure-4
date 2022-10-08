class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        bool check = true;
        int c = matrix[0].size();
		for(int i =0;i<matrix.size();i++){
           if(check){
                for(int j = 0;j<c;j++){
                    if(matrix[0][j]<= target and target<=matrix[i][c-1]){
                        if(matrix[i][j]==target)
                        	return true;
                    	else if(matrix[0][j]>target)
                        	check = false;
            		}	
        		}		
           }else break;
     	}
    return false;
    }
};
        /*
        == COMMON APPROACH ==

        for(int i = 0;i<matrix.size();i++){
            for(int j  = 0;j<matrix[0].size();j++){
                if(matrix[i][j]==target){
                    return true;
                }
            }

        
        }*/
