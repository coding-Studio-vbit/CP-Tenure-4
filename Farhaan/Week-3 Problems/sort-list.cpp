class Solution {
public:
    ListNode* sortList(ListNode* head) {
        
        ListNode *root=NULL;
        
        if(!head)
            return NULL;
        else if(head->next==NULL)
            return head;
        else{
            vector<int> v;
            while(head){
            v.push_back(head->val);
            head=head->next;
            }
            sort(v.begin(), v.end());
            root = new ListNode(v[0]);
            ListNode *t=root;
            for(int i=1; i<v.size(); i++){
            ListNode *r=new ListNode(v[i]);
            t->next=r;
            t=r;
            }
        }
        return root;
    }
};