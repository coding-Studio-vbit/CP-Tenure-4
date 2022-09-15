#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int d,c,suma=0,sumb=0,ta,tb;
        cin>>d>>c;
        int a[3];
        int b[3];
        for(int i = 0;i<3;i++){
            cin>>a[i];
            suma+=a[i];
        }
        for(int i = 0;i<3;i++){
            cin>>b[i];
            sumb+=b[i];
        }
        
        ta = suma+sumb+(d*2);
        
        if(suma<150)
            suma+=d;
        if(sumb<150)
            sumb+=d;
        tb=suma+sumb+c;
        
        if(tb<ta)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    

    return 0;
}
