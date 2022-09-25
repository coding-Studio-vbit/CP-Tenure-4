#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() 
{
  int t;
  cin>>t;
  while(t--)
  {
    deque<char>q;
    int n;
    cin>>n;
   string s; 
   cin>>s;
   int count=0;
   for(int i=0;i<n;i++)
   {
     if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
     {
       count++;
     }
     if(count%2==0)
     {
       q.push_back(s[i]);
     }
     else
     {
       q.push_front(s[i]);
     }
   }
   if(count%2==0)
   {
     while(q.size()>0)
     {
       cout<<q.front();
       q.pop_front();
     }
   }
   else
   {
     while(q.size()>0)
     {
       cout<<q.back();
       q.pop_back();
     }
   }
   cout<<"\n";
  }
	return 0;
}
