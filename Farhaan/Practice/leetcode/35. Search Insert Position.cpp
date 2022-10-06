class Solution {
public:
    
    int binarySearch(vector<int> a, int low, int high, int target){
    if (low<=high) {
        int mid = (low+high)/ 2;
   
        if (a[mid] == target) 
            return mid;

        if (a[mid] > target) 
            return binarySearch(a, low, mid - 1, target);
        
            return binarySearch(a, mid + 1, high, target);
    }
 
    return low;
}
    int searchInsert(vector<int>& nums, int target) {        
        int low = 0;
        int high = nums.size()-1;
        int index = -1;
        int mid;
        int j =   binarySearch(nums, low , high, target);
        return j;
    }
};