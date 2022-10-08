#include <bits/stdc++.h>
using namespace std;

#define farhaan int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
#define ll long long int 

using namespace std;


int main(){
	farhaan{
		int n;
		string s;
		cin>>n>>s;
		deque<char> dq;
		int alice = 0;
		int bob=n-1;
		char t;
		for(int i =0;i<n;i++){
			if(i%2==0){
				t = s[alice];
				if(t=='1') dq.push_back(t);
				else dq.push_front(t);
				alice++;
			}else{
				t = s[bob];
				if(t=='1') dq.push_front(t);
				else dq.push_back(t);
				bob--;
			}

		}
		for(char a: dq)
			cout<<a;
		nl;
	}
}
