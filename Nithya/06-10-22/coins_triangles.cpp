#include <iostream>
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    int n;
	    cin>>n;
	    int height=1;
	    while((height*(height+1))/2<=n)
	    {
	      height++;
	    }
	cout<<height-1<<endl;
	}
	return 0;
}
