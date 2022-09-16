class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1 = headA
        t2 = headB
        count = 0
        while True:   
            if t1 == t2: 
                return t1
            t1 = t1.next
            t2 = t2.next
            if not t1: 
                t1 = headB 
                count += 1
            if not t2: 
                t2 = headA
            if count > 1: 
                return None