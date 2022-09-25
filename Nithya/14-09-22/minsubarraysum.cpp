class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums)
    {
       int length=nums.size();
    int i=0;
        int j=0;
        int sum=0;
        int minimum=INT_MAX;
        while(j<length)
        {
            sum=sum+nums[j];
            if(sum>=target)
            {
                while(sum>=target)
                {
                    sum=sum-nums[i];
                    i++;
                }
                minimum=min(minimum,j-i+2);
            }
            j++;
        }
        return minimum==INT_MAX?0:minimum;
    }
};