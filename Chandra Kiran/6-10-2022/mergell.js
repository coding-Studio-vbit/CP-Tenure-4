/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {


    let head = new ListNode();
    let oghead;

    while (list1 != null && list2 != null) {
        if (list1.val <= list2.val) {
            head.val = list1.val;
            list1 = list1.next;
        }
        else {
            head.val = list2.val;
            list2 = list2.next;
        }

        head.next = new ListNode();
        if (oghead == null) {
            oghead = head;
        }
        head = head.next;
    }
    while (list1 !== null) {
        if (oghead == null) {
            oghead = head;
        }
        head.val = list1.val;
        list1 = list1.next;
        if (list1 != null) {
            head.next = new ListNode();
            head = head.next;
        }

    }
    while (list2 !== null) {
        if (oghead == null) {
            oghead = head;
        }
        head.val = list2.val;
        list2 = list2.next;
        if (list2 != null) {
            head.next = new ListNode();
            head = head.next;
        }
    }
    return oghead === undefined ? null : oghead;
};