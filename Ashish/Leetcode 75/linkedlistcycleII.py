# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = []
        while a:
            if a in b:
                return a
            else:
                b.append(a)
                a = a.next
        return None