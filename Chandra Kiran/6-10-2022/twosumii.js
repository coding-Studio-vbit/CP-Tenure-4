/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
    for (i in numbers) {
        const res = bsearch(numbers, (target - numbers[i]),i);
        if (res) {
            return [parseInt(i)+1, res+1];
        }
   }
};

var bsearch = function (nums, target,i) {
    low = 0;
    high = nums.length - 1;
    while (low <= high) {
        mid = Math.ceil((low + high) / 2);
        if (nums[mid] == target) {
            if (mid != i)
                return mid;
            return mid + 1;
        }
        else if (nums[mid] > target) {
            high = mid - 1;
        }
        else if (nums[mid] < target) {
            low = mid + 1;
        }
    }
    return 0;
}

console.log(twoSum([1, 3,4,4], 8));