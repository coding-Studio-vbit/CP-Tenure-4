#include <bits/stdc++.h>
using namespace std;



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











