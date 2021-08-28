#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define debug(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 50;

int board[MX][MX];
int dice[] = {0,0,0,0,0,0,0};
int rolls[5][7] = {
    {0,0,0,0,0,0,0},
    {0,4,2,1,6,5,3},
    {0,3,2,6,1,5,4},
    {0,5,1,3,4,6,2},
    {0,2,6,3,4,1,5}
};

int dirs[5][2] = {
    {0,0},
    {0,1},
    {0,-1},
    {-1,0},
    {1,0}
};

void move(int dir){
    int temp[7];

    FOR(i,1,7){
        temp[i] = dice[rolls[dir][i]];
        
        // cout << rolls[dir][i];
    }
    // cout << "temp : "; 
    FOR(i,1,7){
        dice[i] = temp[i];

    }

    cout <<temp[1] << '\n';

    
}

void solve(){
    int h,n,a,b,m;

    cin >> h >> n >> a >> b >> m;

    REP(i,h){
        REP(j,n){
            cin >> board[i][j];
        }
    }

    REP(i,m){
        int k; cin >> k;
        int tx,ty;
        tx = dirs[k][0];
        ty = dirs[k][1];
        int nx = a + tx;
        int ny = b + ty;
        if(0 <= nx && nx < h && 0 <= ny && ny < n){
            move(k);
            if(board[nx][ny] == 0){
                board[nx][ny] = dice[6];
            }
            else{
                dice[6] = board[nx][ny];
                board[nx][ny] = 0;
            }
            // cout << "dice : "; 
            // FOR(i,1,7){
            //     cout << dice[i];
            // }

            a = nx;
            b = ny;
        }
        
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}