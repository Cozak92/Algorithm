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
int limit = 0;
queue<pii> virus;

void bfs(){
    int temp[MX][MX];
    REP(i,n)
    REP(j,m) temp[i][j] = lab[i][j];
    int x,y,nx,ny;
    queue<pii> q = virus;
    
    while(!q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();

        REP(i,4){
            nx = x + dx[i];
            ny = y + dy[i];
            if(0 <= nx && nx < n && 0 <= ny && ny < m && temp[nx][ny] == 0){
                temp[nx][ny] = 2;
                q.push(make_pair(nx,ny));
            }
        }

    }
    int cnt = 0;
    REP(i,n)
    REP(j,m) if(temp[i][j] == 0) cnt++;
    
    ans = max(ans,cnt);

}

void build(int walls){
    if(walls == 3){
        bfs();
        return;
    }
    REP(i,n)
    REP(j,m){
        if(lab[i][j] == 0){
            lab[i][j] = 1;
            build(walls + 1);
            lab[i][j] = 0;
        }
    }
    
   

}

void solve(){
    cin >> n >> m;

    REP(i,n)
    REP(j,m){
         cin >> lab[i][j];
         if(lab[i][j] == 2) virus.push(make_pair(i,j));
    }

    build(0);
    cout << ans;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
    
}