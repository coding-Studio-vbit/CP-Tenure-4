#include <iostream>
using namespace std;
int main() {
   int t,i;
	cin>>t;
	while(t--)
	{
	    int n,k,count=0,no_of_naps=0;
	    cin>>n>>k;
	    string str;
	    cin>>str;
	    for(i=0;i<n;i++)
	    {
	      if(str[i]=='0')
	      {
	      count++;
	      if(count>=k)
	      {
	      no_of_naps++;
	      count=0;
	    }
	      }
	      else
	      count=0;
	}
	cout<<no_of_naps<<endl;
	}
	
	return 0;
}
	    