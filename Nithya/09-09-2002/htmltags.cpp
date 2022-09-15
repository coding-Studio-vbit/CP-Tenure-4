#include <iostream>
#include <cstring>
#include<cctype>
using namespace std;
int main()
{
int t,i;
    cin>>t;
   while(t--)
    {
      string tag;
     int flag=0;
     cin>>tag;
    int length=tag.length();
//for(i=2;i<length;i++)
if(tag[0]=='<'&&tag[1]=='/'&&tag[length-1]=='>') 
{
for(i=2;i<length-1;i++)
{
  if((tag[i]>=97&&tag[i]<=122)||(tag[i]>=48||tag[i]<=57))
  {
    flag=1;
  }
  else
  {
    flag=0;
    break;
  }
}
}
if(flag==1)
  cout<<"Success"<<endl;
  else
  cout<<"Error"<<endl;
}
    return 0;
}