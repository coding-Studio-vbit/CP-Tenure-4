class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int c=0;
        int flag = 1;
        while(flag){
            int m = 100;
            flag = 0;
            for(int i=0; i<nums.size(); i++){
                if(nums[i] < m && nums[i]!=0){
                    m = nums[i];
                }
                if(nums[i] != 0){
                    flag = 1;
                }
            }
            cout<<m<<" ";
            for(int i=0; i<nums.size(); i++){
                if(nums[i]!=0){
                    nums[i] -= m;
                }
            }
            c++;           
            
        }
       return (c-1);
    }
};