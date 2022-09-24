/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var i =0, j = height.length-1;
    var max = 0, temp = 0;
    while(i!=j){
        temp = Math.min(height[i], height[j]) * (j - i);
        if (temp > max) {
            max = temp;
        }
        if (height[i] < height[j]) {
            i++
        }
        else {
            j--
        }
    }
    return max
};

maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])