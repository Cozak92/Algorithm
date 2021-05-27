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
const int MX = 20;

int room[MX][MX];
int dp[MX][MX][3];
int n;
int ans = 0;


void solve(){
    cin >> n;
    FOR(i,1,n+1)
    FOR(j,1,n+1) cin >> room[i][j];
    memset(dp,0,sizeof(dp));
    dp[1][2][0] = 1;
    FOR(x,1,n+1){
        FOR(y,2,n+1){
            if(!room[x][y]){
                dp[x][y][0] += dp[x][y - 1][0] + dp[x][y - 1][2];
                dp[x][y][1] += dp[x - 1][y][1] + dp[x - 1][y][2];
                if(!(room[x - 1][y] || room[x][y - 1])) {
                    dp[x][y][2] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2];
                }
            }
        }
    }

    cout << dp[n][n][0] + dp[n][n][1] + dp[n][n][2] << "\n";

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}