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
const int MX = 110;
int n,m,k;
int board[MX][MX];
int dp[MX][MX];


bool solve(){
    memset(dp,0,sizeof(dp));
    cin >> n >> m >> k;
    int yTable[MX][MX];
    int xTable[MX][MX];

    FOR(i,1,n+1){
        FOR(j,1,m+1){
            yTable[i][j] = i;
        }
    }
    FOR(j,1,m+1){
        FOR(i,1,n+1){
            xTable[i][j] = j;
        }
    }
    // int sum = 0;
    // FOR(i,1,n+1){
    //     if(i != 1){
    //         sum = 0;
    //         sum += xTable[i]
    //     }
    //     FOR(j,1,m+1){

    //     }
    // }

    queue<pii> q;
    q.push(make_pair(1,1));
    dp[0][0] = 0; 
    int dx2[] = {0,1};
    int dy2[] = {1,0};
    while(!q.empty()){

        int x = q.front().first;
        int y = q.front().second;
        q.pop();
       
    
        REP(i,2){
            int nx = x + dx2[i];
            int ny = y + dy2[i];
            if(dp[nx][ny]) continue;
            if(0 < nx && nx <= n && 0 < ny && ny <= m){
                if(dx[i]){
                    dp[nx][ny] = dp[x][y] + xTable[nx][ny];
                    q.push(make_pair(nx,ny));
                }
                else{
                    dp[nx][ny] = dp[x][y] + yTable[nx][ny];
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
    if(dp[n][m] == k){
        return true;
    }
    return false;
    

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t; cin >> t;

    while(t--) {
        if(solve()) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
    
}