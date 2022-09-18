class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB){
    ListNode *on=headA;
    ListNode *tn=headB;
    int c=0,count=0;
    while(on!=NULL){
        c++;
        on=on->next;
    }
    while(tn!=NULL){
        count++;
        tn=tn->next;
    }
    on=headA;
    tn=headB;
    if(c>count){
        for(int i=0;i<c-count;i++)
        on=on->next;
    }
    else{
        for(int i=0;i<count-c;i++)
        tn=tn->next;
    }
    while(tn!=on){
        if(tn==NULL)
            return NULL;
        if(on==NULL)
            return NULL;
        tn=tn->next;
        on=on->next;
    }
    return on;
    }
};