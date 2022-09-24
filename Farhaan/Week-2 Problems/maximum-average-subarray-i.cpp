class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sum=0,gSum=INT_MIN,s=nums.size();
    
        for(int i=0;i<k;i++)
            sum+=nums[i];

        gSum=sum;

        for(int i=k;i<s;i++){
            sum-=nums[i-k];
            sum+=nums[i];

            gSum=max(gSum,sum);
        }
        return (gSum*1.0)/(k*1.0);
    }
};