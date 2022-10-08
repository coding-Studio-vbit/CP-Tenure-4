/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
var preorder = function (root) {
    let preorder = []
    // console.log()
    if (root) {
        preorder.push([root?.val])
        root?.children.forEach(e => {
            traverse(preorder, e)
        })
    }
    return preorder == undefined ? [] : preorder;
};

const traverse = (array, root) => {
    if (root) {
        array.push(root.val);
        root.children.forEach(e => traverse(array, e));
    }
}

preorder([])