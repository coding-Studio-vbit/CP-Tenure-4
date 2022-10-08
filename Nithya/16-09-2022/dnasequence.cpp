class Solution
 {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> result;
        if(s.length()<=10)
        {
            return result;
        }
        unordered_map<string,int>m;
        for(int i=0;i<=s.length()-10;i++)
        {
            string h=s.substr(i,10);
            m[h]++;
        }
        for(auto x:m)
        {
            if(x.second>1)
            {
                result.push_back(x.first);
            }
        }
        return result;
    }
};