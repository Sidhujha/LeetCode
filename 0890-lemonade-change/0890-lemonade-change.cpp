class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int c5=0,c10=0;
        bool res=true;
        for(int i:bills){
            if(i==5){
                c5++;
            }
            if(i==10){
                if(c5>0){
                    c10++;
                    c5--;
                }
                else{
                    res=false;
                    break;
                }
            }
            if(i==20){
                if(c5>0 && c10>0){
                    c5--;
                    c10--;
                }
                else if(c5>2){
                    c5-=3;
                }
                else{
                    res=false;
                    break;
                }
            }
        }
        return res;
    }
};