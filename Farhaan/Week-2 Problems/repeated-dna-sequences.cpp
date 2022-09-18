class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
       vector<string> a;
        unordered_map<string,int> mp;
        if(s.size()<10)
            return a;       
        
        for(int i = 0;i<s.size()-9;i++){
            string r = s.substr(i,10);
            mp[r]++;
        }
        
        for(auto b :mp)
            if(b.second>1)
                a.push_back(b.first);
        return a;
    };
};