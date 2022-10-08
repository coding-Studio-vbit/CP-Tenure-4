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
 * @return {boolean}
 */
var isValidBST = function (root) {
    let win = true;

    let queue = [];
    let res = [];
    queue.push(root);
    preorder(root, res)

    if (res.length === 1) {
        return true;
    }
    if (res.length !== Array.from(new Set(res)).length)
        return false
    let og = []
    res.forEach(e => og.push(e));
    og.sort(key = (a, b) => a - b)
    console.log(res, og);
    og.forEach((e, index) => {
        if (e !== res[index])
            win = false;
    })
    return Array.from(new Set(res)).length !== 1 ? win : false;
};

var preorder = (root, res) => {
    if (root) {
        if (root.left)
            preorder(root.left, res);
        res.push(root.val);
        if (root.right)
            preorder(root.right, res);
    }

}