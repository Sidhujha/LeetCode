class Solution {
public:
    // void perm(int ind,vector<int> &v,vector<vector<int>> &ve){
    //     if(ind==v.size()){
    //         ve.push_back(v);
    //         return;
    //     }
    //     for(int i=ind;i<v.size();i++){
    //         swap(v[i],v[ind]);
    //         perm(ind+1,v,ve);
    //         swap(v[i],v[ind]);
    //     }
    // }
    void perm(vector<int> &v,vector<int> &ve,vector<vector<int>> &ans,int per[]){
        if(ve.size()==v.size()){
            ans.push_back(ve);
            return;
        }
        for(int i=0;i<v.size();i++){
            if(per[i]==0){
                ve.push_back(v[i]);
                per[i]=1;
                perm(v,ve,ans,per);
                per[i]=0;
                ve.pop_back();
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> ve;
        vector<vector<int>> ans;
        int per[nums.size()];
        for(int i=0;i<nums.size();i++){
            per[i]=0;
        }
        perm(nums,ve,ans,per);
        // perm(0,nums,ans);
        return ans;
    }
};