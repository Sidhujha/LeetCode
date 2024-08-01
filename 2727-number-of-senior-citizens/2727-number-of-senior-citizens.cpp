class Solution {
public:
    int countSeniors(vector<string>& details) {
        int c=0;
        for(auto i:details){
            string s=i.substr(11,2);
            if(s>"60"){
                c++;
            }
        }
        return c;
    }
};