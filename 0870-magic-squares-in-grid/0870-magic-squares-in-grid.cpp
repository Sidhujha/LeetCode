class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int c=0;
        set<int> s;
        if(grid.size()<3 || grid[0].size()<3){
            return c;
        }
        for(int i=0;i<grid.size()-2;i++){
            for(int j=0;j<grid[0].size()-2;j++){
                if(grid[i][j]>0 && grid[i][j]<10){
                    s.insert(grid[i][j]);
                }
                if(grid[i][j+1]>0 && grid[i][j+1]<10){
                    s.insert(grid[i][j+1]);
                }
                if(grid[i][j+2]>0 && grid[i][j+2]<10){
                    s.insert(grid[i][j+2]);
                }
                if(grid[i+1][j]>0 && grid[i+1][j]<10){
                    s.insert(grid[i+1][j]);
                }
                if(grid[i+1][j+1]>0 && grid[i+1][j+1]<10){
                    s.insert(grid[i+1][j+1]);
                }
                if(grid[i+1][j+2]>0 && grid[i+1][j+2]<10){
                    s.insert(grid[i+1][j+2]);
                }
                if(grid[i+2][j]>0 && grid[i+2][j]<10){
                    s.insert(grid[i+2][j]);
                }
                if(grid[i+2][j+1]>0 && grid[i+2][j+1]<10){
                    s.insert(grid[i+2][j+1]);
                }
                if(grid[i+2][j+2]>0 && grid[i+2][j+2]<10){
                    s.insert(grid[i+2][j+2]);
                }
                if(s.size()==9){
                    int sum=grid[i][j]+grid[i][j+1]+grid[i][j+2];
                    if(grid[i][j]+grid[i+1][j]+grid[i+2][j]==sum && grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]==sum && grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]==sum && grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]==sum && grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]==sum && grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]==sum && grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]==sum){
                        c++;
                        s.clear();
                    }
                }
                else{
                    s.clear();
                }
            }
        }
        return c;
    }
};