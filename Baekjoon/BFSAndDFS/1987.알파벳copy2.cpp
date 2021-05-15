#include <iostream>


using namespace std;
int board[21][21];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
char s[22];
int r,c;
int ans = 1;

void dfs(int x,int y,int cnt,int cache){
    ans = max(ans,cnt);
    int nx,ny;
    for( int i =0; i < 4; i++){
        nx = x + dx[i];
        ny = y + dy[i];

        if (0 <= nx && nx < r && 0 <= ny && ny < c){
            int nextCache = 1 << (board[nx][ny] - 'A');
            if( (cache & nextCache) == 0){
                dfs(nx,ny,cnt + 1, cache | nextCache);
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(0);
    cin >> r >> c;

    for (int i =0; i < r; i++){
        cin >> s;
        for (int j=0; j < c; j++){
            board[i][j] = s[j];
        }
    }
    int cur = 1 << (board[0][0] - 'A');
    dfs(0,0,1,cur);
    cout << ans;


}