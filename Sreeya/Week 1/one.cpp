class Solution {
public:
    bool isPalindrome(int x) {
    
    int sum=0,r;
    int t=x;    
    if (x<0) 
        return false;
    while (t>0) {
        r=t%10;
        sum=sum*10+r;
        t/=10;
    }
    return (sum==x);
        
    }
};
