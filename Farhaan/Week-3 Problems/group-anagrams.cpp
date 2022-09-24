class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        vector<vector<string>> ans;
        unordered_map<string,vector<string>> m;
        
        for(auto  i : strs){
            string temp = i;
            sort(temp.begin(),temp.end());
            m[temp].push_back(i);
        }
        
        for(auto it : m)
            ans.push_back(it.second);
        
        
        return ans;
        
       /* 
       
       ***TLE***
       
       
       vector<vector<string>> finalAnagrams;
        vector<string> str ;
        vector<string> anagrams;
        
        for(auto i:strs){
            string s = i;
            sort(s.begin(),s.end());    
            str.push_back(s);
           // cout<<s<<endl;
        }   
        
        int n =strs.size();
        for(int i =0;i<n;i++){
            if(str[i]=="0")
                    continue;
            anagrams.push_back(strs[i]);

            for(int j =0;j<n;j++){
                if(str[j]=="0")
                    continue;
                if(i==j)
                    continue;
                if(str[i]==str[j]){
                    anagrams.push_back(strs[j]);
                    str[j]="0";
                }
            }
            finalAnagrams.push_back(anagrams);
            anagrams.clear();
            str[i]="0";
            /*cout<<"-------"<<endl;
            for(auto i:str){
                cout<<i<<endl;
            }
        }
        
        
        
        return finalAnagrams;*/
        
    }
};