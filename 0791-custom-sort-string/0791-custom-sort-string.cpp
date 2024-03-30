class Solution {
public:
    string customSortString(string order, string s) {
        string res = "";
        for (char i : order) {
            size_t c = count(s.begin(), s.end(), i);
            if (s.find(i) != string::npos) {
                res.append(c, i);
            }
        }
        for (char i : s) {
            size_t c = count(s.begin(), s.end(), i);
            if (res.find(i) == string::npos) {
                res.append(c, i);
            }
        }
        return res;
    }
};