class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
            return false;
        int a=x;
        long int y=0;
        while(a){
            y =(y*10)+(a%10);
            a/=10;
        }
       return x==y;
    }
};