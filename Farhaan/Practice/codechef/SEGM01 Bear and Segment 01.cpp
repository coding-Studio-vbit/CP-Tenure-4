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
	farhaan{
		string s;
		cin>>s;
		bool has1 = false;
		bool oneafter0 = false;
		bool no = false;
		for(int i =0;i<s.size();i++){
			if(s[i]=='1') has1 = true;
			if(has1 and s[i]=='0') oneafter0 = true;
			if(oneafter0 and s[i]=='1') no = true;
		}
		if(no) cout<<"NO"<<endl;
		else if(!has1) cout<<"NO"<<endl;
		else cout<<"YES"<<endl;		
	}
}