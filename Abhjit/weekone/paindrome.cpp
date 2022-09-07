// problem link https://leetcode.com/problems/palindrome-number/
#include <iostream>
using namespace std;
class Solution {
public:
    bool isPalindrome(int x) {
     int c,a=0,q;
        q=x;
       for(int i = 0;x>0;x=x/10){
          c=x%10;
          a=(a*10)+c; 
        }
        
        if(a == q){
        return true;
        }
        else{
            return false;
        }
    }
};
