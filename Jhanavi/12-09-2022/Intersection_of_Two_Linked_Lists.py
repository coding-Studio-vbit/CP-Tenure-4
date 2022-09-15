class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr_a = headA
        ptr_b = headB
        
        while ptr_a != ptr_b:
            ptr_a = headB if not ptr_a else ptr_a.next
            ptr_b = headA if not ptr_b else ptr_b.next
            
        return ptr_a
