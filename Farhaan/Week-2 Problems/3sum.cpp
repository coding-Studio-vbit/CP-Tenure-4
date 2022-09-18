class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output ;
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size();i++){
            int left = i+1 ;
            int right = nums.size()-1;
            while(left < right){
                if(nums[i]+nums[left]+nums[right] == 0){
                    output.push_back({nums[i],nums[left],nums[right]});
                    int x = nums[left] ;
                    int y = nums[right] ;
                    while(left<right && nums[left] ==x){
                        left++ ;
                    }
                    while(left<right && nums[right] ==y){
                        right-- ;
                    }
                }else if(nums[i]+nums[left]+nums[right] > 0){
                    right --;
                }else {
                    left ++;
                }
            }
            while(i+1 < nums.size() && nums[i] == nums[i+1]){
                i++;
            }
        }
        return output ;
    }
};