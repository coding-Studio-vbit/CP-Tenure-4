#include <bits/stdc++.h>
#define testcases int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int;
using namespace std;
int main(){
	
	testcases{
		long long n,k; cin>>n>>k;
		vector<long long> a(n),ans(k);
		
		for(int i=0;i<n;i++) cin>>a[i];
		
		for(int i=0;i<n;i++){
		    ans[(i+1)%k]=max(ans[(i+1)%k],a[i]);
		}
		
		long long out=0;
		
		for(int i=0;i<k;i++) out+=ans[i];
		
		cout<<out<<endl;
				
	}
	
	
	
	return 0;
	
}