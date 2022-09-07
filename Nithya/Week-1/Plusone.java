class Solution {
    public int[] plusOne(int[] digits) {
        int total=digits.length;
        for(int i=total-1;i>=0;i++)
        {
            if(digits[i]<9)
            {
                digits[i]++;
                return digits;
            }
            digits[i]=0;
        }
        int otherwise[]=new int[total+1];
        otherwise[0]=1;
        return otherwise;
    }
}