/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
    if (!root)
        return [];
    let queue = [];
    queue.push(root);
    let res = [];

    while (!queue.length) {
        let res2 = [];
        let size = queue.length;
        for (let i = 0; i < size; i++){
            const ele = queue.shift()
            if (ele.left !==null)
                queue.push(ele.left)
            if (ele.right !== null)
                queue.push(ele.right)
            
            res2.push(ele.val);
        }

        res.push(res2);

    }
    return res;
}


// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

// root = i = 0 -> LC = 2 * i + 1 || RC = 2 * (i+1) -> index = (1,2)
// element 2 = i = 1 -> LC = 3 || RC = 4 - > index = (3,4)
// element 3 = i = 2 -> LC = 5 || RC = 6 -> index = (4,5)
            
