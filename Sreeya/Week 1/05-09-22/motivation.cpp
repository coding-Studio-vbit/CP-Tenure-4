#include <iostream>
using namespace std;

int main() {
	int t,x,n,s[10],r[10],sm,rm=0;
	cin>>t;
	for(int i=0;i<t;i++){
	cin>>n>>x;
	for(int i=0;i<n;i++)
	cin>>s[i]>>r[i];
	}
	sm=x;
	for(int i=0;i<n;i++)
	{
	    if(s[i]<=sm)
	    {
	        if(r[i]>rm)
	        {
	            rm=r[i];
	        }
	    }
	}
	return 0;
}