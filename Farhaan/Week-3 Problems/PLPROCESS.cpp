#include <bits/stdc++.h>
#define farhaan int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int 
using namespace std;

int main(){
	farhaan{ 
		for(int i =0;i<100;i++){
			for(int j = 0;j<100;j++){
				int res  = i&j;
				if(res==11){
					cout<<i<<" "<<j<<" "<<res;
					nl;
				}
			}
		}
	}	
}