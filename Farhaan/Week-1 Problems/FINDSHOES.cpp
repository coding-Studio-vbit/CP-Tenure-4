#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m,r;
        cin>>n>>m;
        if((n-m)<=0)
            r =n;
        else
            r=(n-m)+n;
        cout<<r<<endl;
    }
    return 0;
}
