/**
 * @param {number} n
 * @param {number} k
 * @param {number} maxPts
 * @return {number}
 */
var new21Game = function (n, k, maxPts) {
    let dp = []; 
    sum = 0.0
    for (let i = k; i <= Math.min(n, k + maxPts - 1); i++) {
        dp[i] = 1.0;
        sum += dp[i];
    }

    for (let i = k - 1; i >= 0; i--) {
        dp[i] = sum / maxPts;

        if (i + maxPts < dp.length) {
            sum -= dp[i + maxPts]
        }
        sum += dp[i]

    }

    return dp[0];
};

// [1,2,3,4,5,6,7,8,9,10] = max points
// n = 21, k = 17, maxPts = 10
// [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
