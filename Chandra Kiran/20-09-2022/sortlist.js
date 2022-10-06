/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function (head) {
    let temp = head;
    let i = 0;
    let arr = [];
    while (temp != null) {
        arr[i++] = temp.val;
        temp = temp.next;
    }
    arr.sort(key = (a, b) => a - b);
    temp = head;
    i = 0;
    while (temp != null) {
        temp.val = arr[i++];
        temp = temp.next;
    }
    return head;
};
