// problem https://www.codechef.com/LP1TO201/problems/IMDB?tab=statement
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	
	int t;
	cin>>t;while(t--){
	    int n,x,s,r,q,ma=0;
	    cin>>n>>x;
	    while(n--){
	        cin>>s>>r;
	        if(s<=x){
	            if(ma<r){
	                ma = r;
	            }
	        }
	        
	    }
	    cout<<ma<<endl;
	}
	return 0;
}
