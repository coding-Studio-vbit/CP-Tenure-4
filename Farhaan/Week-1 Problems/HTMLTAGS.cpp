#include <iostream>
#include <string>
using namespace std;
void check(string str,int last){
      int temp;
      for(int i = 2;i<last;i++){
            temp = str[i];
            if(temp>47 && temp<58)
                continue;
            if(temp<97|| temp>122){
                cout<<"Error"<<endl;
                return;
            }
        }
        cout<<"Success"<<endl;
}
int main(){
    string str;
    int t,last;
    cin>>t;
    while(t--){
       cin>>str;
       last = str.length()-1;
        if(str[0]!='<' || str[1]!='/' || str[last]!='>' || str.length()==3){
            cout<<"Error"<<endl;
            continue;
        }
        check(str,last);
    }
    return 0;
}
