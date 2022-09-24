# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getlen(self, head, length):
        c=length
        if(head == None):
            return c
        
        c+=1
        return self.getlen(head.next, c)
        
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_1 = self.getlen(headA, 0)
        len_2 = self.getlen(headB, 0)       
        
        diff = abs(len_1 - len_2)
        
        if(len_1>len_2):
            while(diff):
                headA = headA.next
                diff-=1

        if(len_2>len_1):
            while(diff):
                headB = headB.next
                diff-=1
                
        while(headA!= None and headB!=None):            
            if(headA == headB):
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None
 