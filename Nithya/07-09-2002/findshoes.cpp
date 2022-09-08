#include <iostream>
using namespace std;

int main()
{
  int t,i;
  cin>>t;
  for(i=0;i<t;i++)
  {
   int n,m;
    cin>>n>>m;
    if(m>=n)
    {
        cout<<n<<endl;
    }
    else if(m==0)
    {
        cout<<n*2<<endl;
    }
    else if(m<n)
    {
        cout<<n+(n-m)<<endl;
    }
    
  }
	return 0;
}
