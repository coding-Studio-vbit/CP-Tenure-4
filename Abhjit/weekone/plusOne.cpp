// problem link https://leetcode.com/problems/plus-one/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> i;
        int t = digits.size()-1;
        int a =digits[t];
        for(int i = t;i>=0;i--){
        if(digits[i] != 9){
           digits[i]=digits[i]+1;
         return digits;
         }
         else{
            digits[i]=0;
        }
        
        
        }
        digits[0]=1;
        digits.push_back(0);
        return digits;     
    }
};
