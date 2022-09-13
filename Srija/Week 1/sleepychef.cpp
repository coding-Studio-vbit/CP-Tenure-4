#include<bits/stdc++.h>
#include<iostream>
using namespace std;

#define ll     long long int

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        string s;
        cin>>s;
        int c = 0, total_naps = 0;
        for(int i=0; i<s.size(); i++){
            if(s[i] == '0')
            {
                c++;
            }
            else{
                total_naps += c/k;
                c=0;
            }
        }
        total_naps += c/k;
        cout<<total_naps<<endl;
        
    }
    
    return 0;
}   
