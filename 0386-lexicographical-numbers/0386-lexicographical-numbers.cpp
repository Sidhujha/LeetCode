class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<string> s;
        for(int i=1;i<=n;i++){
            s.push_back(to_string(i));
        }
        sort(s.begin(),s.end());
        vector<int> v;
        for(auto i:s){
            v.push_back(stoi(i));
        }
        return v;
    }
};