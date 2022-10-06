
var reverseList = function (head) {

    let current = head;
    let prev = null, next = null;

    while (current != null) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }


    return prev;
};