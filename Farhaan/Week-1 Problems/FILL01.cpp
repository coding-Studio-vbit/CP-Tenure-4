#include <iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,k,count=0,naps=0;
        string s;
        cin>>n>>k;
        cin>>s;
        for(int i = 0;i<s.length();i++){
            if(s[i]=='0'){
                count++;
                if(count==k){
                    naps++;
                    count = 0;
                }
            }else 
                count = 0;
        }
        cout<<naps<<endl;
    }
    return 0;
}