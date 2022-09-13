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
    string s;
    while(t--)
    {
        cin>>s;
        int len = s.length();
        int flag = 1;
        if(s[0] =='<' && s[1]=='/' && s[len-1] == '>')
        {
            //cout<<"hi\n";
            for(int i=2;i<len-1;i++)
            {
                int le = int(s[i]);
                //cout<<le<<" ";
                if((le<=57 && le>=48) || (le>=97 && le<=122))
                {
                    flag =1;
                }
                else{
                    
                    flag = 0;
                    break;
                }
            }
            
            if(len == 3)
            {
                flag = 0;
                
            }
        }
        else{
            
            flag =0;
        }
        //cout<<"\n";
        if(flag == 1)
        {
            cout<<"success\n";
        }
        else{
            cout<<"Error\n";
        }
        
    }
    
    return 0;
}   
