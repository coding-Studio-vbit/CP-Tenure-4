#include <bits/stdc++.h>
#define farhaan int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int 
using namespace std;

int main(){
	farhaan{ 
		ll n,sum=0;
        cin>>n;
        ll a[n];
        ll pre[n];
        
        for(int i=0;i<n;i++){
            cin >> a[i];
            sum += a[i];
            pre[i]=sum;
        }
        
        ll res = sum;
        for(int i=0;i<n;i++)
            res = min(max(pre[i],(sum-pre[i])),res);
        
        cout << res << endl;
	}	
}