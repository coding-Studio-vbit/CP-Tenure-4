#include <bits/stdc++.h>
#define tc int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int 
using namespace std;

int main(){
	tc{ 
		ll n,t,count=LLONG_MAX,x,y,z,c;
		cin>>n;
		int a[n];
		for(int i = 0;i<n;i++)
			cin>>a[i];
					
		sort(a,a+n);
		for(int i =0;i<n-2;i++){
			 x = a[i];
			 y  =a[i+1];
			 z = a[i+2];
			 c = 0;
			while(x<y){
				x++;
				c++;
			}
			while(z>y){
				z--;
				c++;
			}
			count = min(c,count);			
		}
		cout<<count<<endl;
	}	
}