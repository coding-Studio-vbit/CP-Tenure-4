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

int vowel(char a){
	
	if(a == 'a' || a=='e' || a=='i' || a=='o' || a=='u')
	return 1;
	else return 0;
}

int main(){
	farhaan{
		string s;
		cin>>s;
		int cnt = 0;
	 	bool b =false;
		for(int i = 0;i<s.size();i++){
			if(cnt==3){
				b = true;
				break;
			} 
			if(vowel(s[i])) cnt++;
			else cnt = 0;
		}
		if(b) cout<<"Happy"<<endl;
		else cout<<"Sad"<<endl;
	}
	
}











