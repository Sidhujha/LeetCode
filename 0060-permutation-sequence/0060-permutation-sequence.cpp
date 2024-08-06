class Solution {
    public:
        void perm(int ind,vector<int> &v,vector<vector<int>> &res,int k){
            if(res.size()==k+35000){
                return;
            }
            if(ind==v.size()){
                res.push_back(v);
                return;
            }
            for(int i=ind;i<v.size();i++){
                swap(v[i],v[ind]);
                perm(ind+1,v,res,k);
                swap(v[i],v[ind]);
            }
        }
public:
    string getPermutation(int n, int k) {
        vector<int>v;
        vector<vector<int>> res;
        for(int i=1;i<=n;i++){
            v.push_back(i);
        }
        perm(0,v,res,k);
        sort(res.begin(),res.end());
        string s="";
        for(int i:res[k-1]){
            s+=to_string(i);
        }
        return s;
    }
};