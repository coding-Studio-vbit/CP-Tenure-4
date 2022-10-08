var detectCycle = function (head) {

    while (head != null) {
        if (head.val !== 666) {
            head.val = 666;
            head = head.next;
            continue;
        }
        return head;
    }
    return null;
};