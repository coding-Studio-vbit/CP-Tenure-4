#include <iostream>
using namespace std;
int main() {
int t,i;
  cin>>t;
  for(i=0;i<t;i++)
  {
    int a,b,c;
    cin>>a>>b>>c;
    if(a>b&&a<c||a<b&&a>c)
    cout<<a<<endl;
    else if(b>c&&b<a||b<c&&b>a)
    cout<<b<<endl;
    else
    cout<<c<<endl;
  }
      