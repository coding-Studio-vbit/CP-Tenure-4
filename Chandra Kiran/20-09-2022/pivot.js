var pivotIndex = function (nums) {
    let i = 0, j;
    let leftSum = 0, sum = 0, rightSum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
    }
    while (i < nums.length) {
        if (leftSum === (sum - leftSum - nums[i])) {
            return i;
        }
        leftSum += nums[i];
        i++;
    }
    return -1;

};

console.log(pivotIndex([1, 7, 3, 6, 5, 6]));

// var pivotIndex = function(nums) {
//     let i, j;
//     let leftSum = 0;
//     let rightSum = 0;
//     for (i = 0; i < nums.length; i++) {
//         leftSum = 0;
//         rightSum = 0;
//         for (j = 0; j < i; j++) {
//             leftSum += nums[j];
//         }
//         for (j = i + 1; j < nums.length; j++) {
//             rightSum += nums[j];
//         }
//         if (leftSum === rightSum) {
//             return i;
//         }
//     }
//         return -1;

// };