var searchInsert = function (nums, target) {

    low = 0;
    high = nums.length - 1;
    while (low <= high) {
        mid = Math.ceil((low + high) / 2);
        if (nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] > target) {
            high = mid - 1;
        }
        else if (nums[mid] < target) {
            low = mid + 1;
        }
    }
    if (target > nums[mid])
        return mid + 1;
    else if (target < nums[mid])
        return mid;

};