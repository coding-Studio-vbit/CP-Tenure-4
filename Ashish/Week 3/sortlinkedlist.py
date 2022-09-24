# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        while head:
            values.append(head.val)
            head = head.next
        values.sort()
        values = collections.deque(values)
        head = node
        while head:
            head.val = values.popleft()
            head = head.next
        return node