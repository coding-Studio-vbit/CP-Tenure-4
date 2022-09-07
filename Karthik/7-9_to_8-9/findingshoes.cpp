#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        int N,M;
        cin>>N>>M;
        if(N>M)
        cout<<(N*2)-M<<endl;
        else
        cout<<N<<endl;
    }
    return 0;
}