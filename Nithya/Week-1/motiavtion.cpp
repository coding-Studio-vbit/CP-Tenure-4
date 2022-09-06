#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n,x;
	    cin>>n>>x;
	    int space[n],rating[n];
	    for(i=0;i<n;i++)
	    {
	        cin>>space[i]>>rating[i];
	    }
	    int highest=0;
	    for(i=0;i<n;i++)
	    {
	        if(rating[i]>=highest&&space[i]<=x)
	        {
	          highest=rating[i];  
	        }
	    }
	        cout<<highest<<endl;
	}
	return 0;
}
