#include <bits/stdc++.h>
using namespace std;
//debugging template
void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}
template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif


#define farhaan int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int 

using namespace std;


int main(){
	int n ;
	cin>>n;
	int t,t1; 
	pair<bool,bool> pr[n];
	int odd1=0,odd2=0;
	bool checkFor1 = false;	
	
	for(int i = 0;i<n;i++){
		cin>>t>>t1;
		
		if(n==1 and t==0 and t1==0){
			cout<<-1;
			return 0;
		}
			if(t&1)
				odd1++;
			if(t1&1)
				odd2++;
			if((t&1 and t1%2==0 )or (t%2==0 and t1&1 ))
			checkFor1 = true;
	}
	

	debug(odd1,odd2);
	
	if(odd1%2==0 and odd2%2==0 )cout<<0;
	else if(odd1&1 and odd2&1 and checkFor1)cout<<1;
	else cout<<-1;
	return 0;

}











