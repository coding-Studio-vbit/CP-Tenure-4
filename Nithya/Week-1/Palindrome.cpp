class Solution {
public:
    bool isPalindrome(int x) {
        long int r,sum=0,original;
        original=x;
        while(x>0)
        {
            r=x%10;
            sum=(sum*10)+r;
            x=x/10;
        }
        if(original==sum)
        return true;
        else
            return false;
        
        
    }
};