#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int> v(n);
        for(int i=0;i<n;i++)
        {
            cin>>v[i];
        }
        sort(v.begin(),v.end());
        int maximum=INT_MAX;
        for(int i=1;i<n-2;i++)
        {
            maximum=min(maximum,v[i]-v[i-1]-v[i-1]-v[i]);
        }
        cout<<maximum<<endl;
    }
    return 0;
}