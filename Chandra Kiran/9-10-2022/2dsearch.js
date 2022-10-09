/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
    let low = 0, high = matrix.length, i, j;

    while (low < high) {
        i = 0;
        j = matrix[low].length - 1;
        console.log(matrix[low], i, j)
        while (i <= j) {
            let mid = Math.floor((i + j) / 2)
            if (target === matrix[low][mid]) {
                return true;
            }
            else if (target < matrix[low][mid]) {
                j = mid - 1;
            }
            else if (target > matrix[low][mid]) {
                i = mid + 1;
            }
        }
        low++;
    }
    return false;
}