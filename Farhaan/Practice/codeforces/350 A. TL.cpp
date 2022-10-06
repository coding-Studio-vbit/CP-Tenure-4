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
	
	int n, m, minc=101, maxc=0, minw=101;
	cin>>n>>m;
	vector<int> correct(n);
	vector<int> wrong(m);
	
	for(int i =0;i<n;i++){
		cin>>correct[i];	
		minc= min(correct[i], minc);
		maxc= max(correct[i],maxc);
	}
	
	for(int i =0;i<m;i++){
		cin>>wrong[i];	
		minw = min(minw, wrong[i]);
	}
	
	int ans = max(2*minc, maxc);
	
	if(ans<minw) cout<<ans;
	else cout<<-1;
	
}