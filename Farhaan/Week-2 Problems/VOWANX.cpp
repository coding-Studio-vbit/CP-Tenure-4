#include <bits/stdc++.h>
#define testcases int tz;cin>>tz;while(tz--)
#define nl cout<<endl;
using namespace std;

int main(){
	testcases{ 
		int n,l,r,t;
		cin>>n;
		char a[n];
		deque<char> res;
		int count = 0;
		
		for(int i =0;i<n;i++){
			cin>>a[i];
			char t = a[i]; 
			if(t=='a' ||t=='e' || t=='i'|| t=='o'||t=='u')
				count++;
			
			if(count%2==0)
				res.push_back(t);
			else
				res.push_front(t);
			
		}
		/*for(int i = 0;i<n;i++) {
			cin>>a[i];
			if((a[i]=='a' ||a[i]=='e' || a[i]=='i'|| a[i]=='o'||a[i]=='u') && i!=0)
				vowels.push_back(i); 
		}
		
		for(int i = 0;i<vowels.size();i++){ 
			l=0,r=vowels[i]-1;
			while(l<r){
				if(l==r)
					break;
				t = a[l];
				a[l]=a[r];
				a[r]=t;
				
				l++;
				r--;
			}
		}
			
		/*for(int i = vowels.size()-1;i>=0;i--){
			cout<<vowels[i];
		}
		nl;*/
		if(count%2==0)
			for(auto c : res)
				cout<<c;
		else
			for(int i =res.size()-1;i>=0;i--)
				cout<<res[i];
		nl;
	}	
}