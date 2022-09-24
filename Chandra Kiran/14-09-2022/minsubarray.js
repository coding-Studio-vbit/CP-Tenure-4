/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
    var i = 0, j = 0, temp = 0;
    var len = 0, tempval = 0,sum = 0;
    let res = []
    while (j < nums.length) {
        sum += nums[j]
        
            while (sum > target && sum - nums[i] >= target) {
                sum -= nums[i]
                i++
            }
        if (sum >= target) 
            res.push([j - i+1, i, j])
            
        
        j++
    }
    if (res.length === 0) {
        return 0
    }
    res = res.sort((a,b)=>a[0] - b[0])
    return res[0][0]
};

console.log(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
console.log(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))