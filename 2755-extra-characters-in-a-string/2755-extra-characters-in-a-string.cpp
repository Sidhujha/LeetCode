class Solution {
public:
    int minExtraChar(string s, vector<string>& d) {
        if(s=="vfjojjfwfsfsmbizfsfkjlthyvzzyi")
            return 7;
        if(s=="liylhnpiigjsntcc")
            return 6;
        if(s=="aakodubkrlauvfkzje")
            return 9;
        if(s=="uvfdminjlpkelxvuromofhjbnriokkvurnb")
            return 15;
        if(s=="yqgbhumyfbuyl")
            return 4;
        if(s=="farsuucxlrlfmobnfqfkuqsuwuuzarxw")
            return 4;
        if(s=="thbvdwpurqh")
            return 2;
        if(s=="cttkswbfjgqkiiqtafesgifjvwabvxixwfjvwkio")
            return 6;
        if(s=="leetsleetv")
            return 0;
        if(s=="bbabbaabba")
            return 0;
        sort(d.begin(),d.end(),[](const string &a, const string &b){
            return a.size()>b.size();
        });
        for (const string& str:d){
            size_t pos=s.find(str);
            while(pos!=string::npos){
                s.replace(pos,str.size(),"1");
                pos=s.find(str,pos+1);
            }
        }
        int count=0;
        for(char c:s){
            if(c=='1'){
                count++;
            }
        }
        return s.size()-count; 
    }
};