#include <iostream>
#include<algorithm>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        long int n;
        cin>>n;
       long int a[n],b[n]={0},sum=0;
        for(int i=0;i<n;i++)
        {
        cin>>a[i];
        sum=sum+a[i];
        }
       long int p=0;
        long int x;
        long int z;
        for(int i=0;i<n;i++)
        {
          p=p+a[i];
          x=sum-p;
          z=max(p,x);
          b[i]=z;
        }
        sort(b,b+n);
        cout<<b[0]<<endl;
    }
	return 0;
}
