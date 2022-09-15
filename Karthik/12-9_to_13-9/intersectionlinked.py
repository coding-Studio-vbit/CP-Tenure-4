# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=headA
        count1=0
        count2=0
        b=headB
        while a:
            count1+=1
            a=a.next
        while b:
            count2+=1
            b=b.next
        if count1>count2:
            for i in range(count1-count2):
                headA=headA.next
        elif count2>count1:
            for i in range(count2-count1):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return headA
        
        