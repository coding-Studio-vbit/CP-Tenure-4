var middleNode = function (head) {

    let i = 0, j = 0;
    let temp = head;
    while (temp != null) {
        i++;
        temp = temp.next;
    }
    temp = head;
    while (j !== i / 2) {
        temp = temp.next;
    }

    return temp;
};