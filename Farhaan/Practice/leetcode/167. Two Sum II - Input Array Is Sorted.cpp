class Solution {
public:
    
   /* int binaryS(vector<int> a, int l, int h,int x){
        int low = l,high = h ; 
        while(low <= high){
            int mid = (low + high) / 2;
            if (x < a[mid])
                high = mid - 1;
            else if (x > a[mid])
                low = mid + 1;
            else
            return mid;
       }
        return -1;
    }
    
*/
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        int n = nums.size();
        int i = 0, j = nums.size()-1;
        while(i<j){
            if(nums[i]+nums[j]==target){
                res.push_back(i+1);
                res.push_back(j+1);
                break;
            }else if(nums[i]+nums[j]>target) j--;
            else i++;
        }
       /* for( i =1;i<n;i++){
        
        j = binaryS(nums, 0, i-1,target-nums[i]);   
            if(j ==-1 )
                continue;
            break;
        }
        res.push_back(j+1);
        res.push_back(i+1);
        cout<<j<<" "<<i<<endl;*/
            
       
        return res;
        
    }
};