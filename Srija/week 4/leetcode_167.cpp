#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size()-1;
        vector<int> ans;
        int s;
        while(left<right){
            s = numbers[left]+numbers[right];
            if(s == target){
                ans.push_back(left+1);
                ans.push_back(right+1);
                break;
            }
            else if(s < target)
                left+=1;
            else
                right-=1;
        }
        return ans;
    }
};