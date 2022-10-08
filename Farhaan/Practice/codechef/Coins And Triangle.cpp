#include <bits/stdc++.h>
using namespace std;

#define farhaan int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int 

using namespace std;


int main(){
	farhaan{
		int n ,f;
		cin>>n;
		int sum=0;
		int level = 1;
		while(sum<=n){
			sum = sum+level;
			debug(level);
			level++;
		}

		cout<<level-2<<endl;
		
		
	}
}











