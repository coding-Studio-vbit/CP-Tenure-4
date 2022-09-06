class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n=digits.size();
        int max=0,l;
        for(int i=0;i<n;i++)
        {
            if(digits[i]>max)
            {   max=digits[i];
             l=i;}
        }
        digits[l]+=1;
        return digits;
    }
};