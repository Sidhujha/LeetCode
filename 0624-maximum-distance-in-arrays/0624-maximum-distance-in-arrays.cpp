class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int a=arrays[0][0];
        int b=arrays[0].back();
        int res=0;
        for(int i=1;i<arrays.size();i++){
            res=max(res,abs(arrays[i].back()-a));
            res=max(res,abs(arrays[i][0]-b));
            a=min(a,arrays[i][0]);
            b=max(b,arrays[i].back());
        }
        return res;
    }
};