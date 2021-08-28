#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 10;

int n,m;
int board1[MX][MX];
int board2[MX][MX];
vector<pii> camera;
int ans = 0;

void upd(int x, int y,int dir){
    dir %= 4;

    while(true){
        x += dx[dir];
        y += dy[dir];

        if( 0 <= x && x < n && 0 <= y && y < m){
            if(board2[x][y] == 6) return;
            if(board2[x][y] != 0) continue;
            board2[x][y] = 7;
        }
        else return;
    }
}

void solve(){
    cin >> n >> m;

    REP(i,n)
    REP(j,m) {
    cin >> board1[i][j];
    if(board1[i][j] != 6 && board1[i][j] != 0){
        camera.push_back(make_pair(i,j));
    }
    else ans++;
    }


    for(int k = 0; k < (1<<(2 * camera.size())); k++){
        int temp = k;
        REP(i,n)
        REP(j,m) board2[i][j] = board1[i][j];

        for(auto pos : camera){
            int dir = temp % 4;
            temp /= 4;
            int x = pos.first;
            int y = pos.second;

            if(board2[x][y] == 1){
                upd(x,y,dir);
            }
            if(board2[x][y] == 2){
                upd(x,y,dir);
                upd(x,y,dir + 2);
            }
            if(board2[x][y] == 3){
                upd(x,y,dir);
                upd(x,y,dir + 1);
            }
            if(board2[x][y] == 4){
                upd(x,y,dir);
                upd(x,y,dir + 1);
                upd(x,y,dir + 2);
            }
            if(board2[x][y] == 5){
                upd(x,y,dir);
                upd(x,y,dir + 1);
                upd(x,y,dir + 2);
                upd(x,y,dir + 3);
            }
        }
        int cnt = 0;
        REP(i,n)
        REP(j,m) if(board2[i][j] == 0) cnt++;

        ans = min(ans,cnt);

    }
    
    cout << ans << "\n";
    
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    solve();
}