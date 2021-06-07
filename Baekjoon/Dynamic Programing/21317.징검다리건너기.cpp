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
constexpr double DINF = 1.79769e+308;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 30;

int n;
int stone[MX][2];
int dp[MX][2];


void solve(){
    cin >> n;
  FOR(i,1,n){
      cin >> stone[i][0] >> stone[i][1];
  }
  int k; cin >> k;
    memset(dp,INF,sizeof(dp));
    dp[1][0] = dp[1][1] = 0;
  FOR(i,1,n+1){
      REP(j,2){
          dp[i+1][j] = min(dp[i+1][j],dp[i][j] + stone[i][0]);
          dp[i+2][j] = min(dp[i+2][j],dp[i][j] + stone[i][1]);
      }

      dp[i+3][1] = min(dp[i+3][1],dp[i][0] + k);
  }

    cout << min(dp[n][1],dp[n][0]);

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}