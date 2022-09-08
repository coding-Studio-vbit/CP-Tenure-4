#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int d,c,sum1=0,sum2=0,t1,t2;
        cin>>d>>c;
        int a[3];
        int b[3];
        for(int i = 0;i<3;i++){
            cin>>a[i];
            sum1+=a[i];
        }
        for(int i = 0;i<3;i++){
            cin>>b[i];
            sum2+=b[i];
        }
        
        t1 = sum1+sum2+(d*2);
        
        if(sum1<150)
            sum1+=d;
        if(sum2<150)
            sum2+=d;
        t2=sum1+sum2+c;
        
        if(t1<t2)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    

    return 0;
}
