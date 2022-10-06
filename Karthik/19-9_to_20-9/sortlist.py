# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        b=[]
        tail=head
        main=head
        while(tail):
            b.append(tail.val)
            tail=tail.next
        b.sort()
        for i in b:
            main.val=i
            main=main.next
        # print(main)
        return head
            