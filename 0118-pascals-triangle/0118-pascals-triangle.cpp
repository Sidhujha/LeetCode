class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for(int i=1;i<=numRows;i++){
            int a=1;
            vector<int> temp;
            temp.push_back(1);
            for(int j=1;j<i;j++){
                a=a*(i-j);
                a=a/j;
                temp.push_back(a);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};