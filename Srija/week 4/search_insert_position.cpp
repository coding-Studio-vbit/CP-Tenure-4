#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        int mid;
        int flag = 0;
        int val;
        while(left<=right){
            mid = left + (right-left)/2;
            if(nums[mid] == target)
            {
                flag = 1;
                val = mid;
                break;
            }
            else if(nums[mid] > target)
            { right = mid-1;}
            else if(nums[mid] < target)
            { left = mid+1;}
        }
        
        if(flag == 0)
        {
            if(target < nums[0])
            { val = 0; }
            else if(target > nums[nums.size()-1])
            {  val = nums.size(); }
            else{
                if(nums[mid] < target)
                    val = mid+1;
                else
                    val = mid;
            }
        }
        
        return val;

    }
};