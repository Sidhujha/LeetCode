class Solution {
    public: 
    void sum(int ind, vector<int> &v, vector<int> &ve,vector<vector<int>> &res,int target){
    if(target==0){
        res.push_back(ve);
        return;
    }
    for(int i=ind;i<v.size();i++){
        if(i>ind && v[i]==v[i-1]){
            continue;
        }
        if(v[i]>target){
            break;
        }
        ve.push_back(v[i]);
        sum(i+1,v,ve,res,target-v[i]);
        ve.pop_back();
    }
}
    public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans; 
        vector<int> ds; 
        sum(0, candidates, ds, ans, target); 
        return ans; 
    }
};