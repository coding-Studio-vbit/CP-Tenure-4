var findDuplicate = function (nums) {
    let count = []
    for (let i = 0; i < nums.length; i++) {
        if (count[nums[i]] === undefined)
            count[nums[i]] = 0
        count[nums[i]]++;
    }
    for (let i = 0; i < nums.length; i++) {
        if (count[nums[i]] > 1) {
            return nums[i];
        }
    }
};