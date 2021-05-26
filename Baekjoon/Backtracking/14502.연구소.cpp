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
int lab[MX][MX];
int lab2[MX][MX];
int ans = -INF;
queue<pii> virus;

void bfs(int lab2[][MX]){
    bool isVisited[MX][MX];
    int x,y,nx,ny;
    while(!virus.empty()){
        x = virus.front().first;
        y = virus.front().second;
        virus.pop();

        REP(i,4){
            nx = x + dx[i];
            ny = y + dy[i];
            if(0 <= nx && nx < n && 0 <= ny && ny < m && lab2[nx][ny] == 0){
                lab2[nx][ny] = 2;
                virus.push(make_pair(nx,ny));
            }
        }

    }

}

void build(int tot,int walls){

    if(walls = 3){
        REP(i,n)
        REP(j,m) lab2[i][j] = lab[i][j];
        bfs(lab2);
        int cnt = 0;
        REP(i,n)
        REP(j,m) if(lab2[i][j] == 0) cnt++;
        ans = max(ans,cnt);
        return;
    }
    
    int x = tot / 8;
    int y = tot % 8;

    if(lab[x][y] == 0){
        for(int i = tot + 1; i < 64; i++){
            lab[x][y] = 1;
            build(i,walls + 1);
            lab[x][y] = 0;
        }
    }
    else build(tot + 1, walls);

}

void solve(){
    cin >> n >> m;

    REP(i,n)
    REP(j,m){
         cin >> lab[i][j];
         if(lab[i][j] == 2) virus.push(make_pair(i,j));
    }

    build(0,0);

}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}