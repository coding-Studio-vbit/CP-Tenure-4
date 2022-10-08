class Solution {
    public double findMaxAverage(int[] nums, int k)
    {
        int i=0,j=0;
        double sum=0,max=Double.NEGATIVE_INFINITY;
        for(j=0;j<nums.length;j++)
        {
            sum=sum+nums[j];
            if((j-i+1)==k)
            {
                if(sum>max)
                {
                    max=sum;
                }
                sum=sum-nums[i];
                i++;
            }
        }
        return max/k;
    }
}