class Solution {
public:
    int minBitFlips(int s, int g) {
        string s1="";
        string s2="";
        while(s>0){
            s1+=to_string(s%2);
            s/=2;
        }
        while(g>0){
            s2+=to_string(g%2);
            g/=2;
        }
        int diff=abs(int(s1.length())-int(s2.length()));
        if(s1.length()>s2.length()){
            for(int i=0;i<diff;i++){
                s2+='0';
            }
        }
        else{
            for(int i=0;i<diff;i++){
                s1+='0';
            }
        }
        int c=0;
        for(int i=0;i<s1.length();i++){
            if(s1[i]!=s2[i]){
                c+=1;
            }
        }
        return c;
    }
};