#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n ,x,s,r,maxr=0,maxs=0;
        cin>>n>>x;
        for(int i = 0;i<n;i++){
            cin>>s>>r;
            if(s<=x && r>=maxr){
            maxr = r;
            maxs = s;
            }
        }
        cout<<maxr<<endl;
    }
    return 0;
}
