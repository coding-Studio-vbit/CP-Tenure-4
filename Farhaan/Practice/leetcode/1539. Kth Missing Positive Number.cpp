class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        vector<int> all(10001);
        vector<int> missing;
        for(int i :arr) all[i]=1;
        for(int i = 1;i<=arr.back();i++){
            if(all[i]==0) missing.push_back(i);
            if(missing.size()==k) return missing.back();
        }
        return (arr.back()+(k-missing.size()));
    }
};