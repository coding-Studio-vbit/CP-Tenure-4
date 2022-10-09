var lowestCommonAncestor = function (root, p, q) {

    if (!root) return root;

    if (root.val === p.val || root.val === q.val) {
        return root;
    }

    let minimum = Math.min(p.val, q.val);
    let maximum = Math.max(p.val, q.val);

    if (root.val > minimum && root.val < maximum) {
        return root;
    }

    if (root.val > maximum) {
        return lowestCommonAncestor(root.left, p, q);
    }
    return lowestCommonAncestor(root.right, p, q)
};
