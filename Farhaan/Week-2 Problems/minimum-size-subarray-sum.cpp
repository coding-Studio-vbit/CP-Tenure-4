class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
    int n=nums.size(),len=INT_MAX;
        int i=0,j=0,sum=nums[0];
        while(i<n&&j<n){
            if(sum>=target)  
            	len=min(len,j-i+1);
            if(sum>target){
                sum-=nums[i];
                i++;
            }else{
                j++;
                if(j<n) 
                	sum+=nums[j];
            }
        }
        if(len==INT_MAX)   
        	return 0;
        return len;
    }
};