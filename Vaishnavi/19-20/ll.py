class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        res.sort()
        ll = ListNode()
        temp = ll
        for i in res:
            temp.next = ListNode(i)
            temp = temp.next
        return ll.next