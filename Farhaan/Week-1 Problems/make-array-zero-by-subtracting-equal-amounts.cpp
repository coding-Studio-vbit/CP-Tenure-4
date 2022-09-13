class Solution {
public:

	//vector-->set can be used to reduce time complexity
	
    int minimumOperations(vector<int>& nums) {
        int smallest=0,flag = 1,count = 0;
        sort(nums.begin(),nums.end());        
        while(flag==1) { 
            flag = 0;
            for(auto i :nums){
                if(i!=0){
                    smallest = i;
                    flag = 1;
                    count++;
                    break;
                }
            }
            if(flag==1){ 
                for(int i = 0;i<nums.size();i++){        
                      if(nums[i]>0)
                        nums[i]-=smallest;
                }
            }
        }   
        return count ;   
    }
};