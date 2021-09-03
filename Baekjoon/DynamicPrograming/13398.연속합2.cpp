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
const int MX = 100010;

int arr[MX];
int dp[MX][2];

void solve(){
  int n; cin >> n;
  FOR(i,1,n+1) cin >> arr[i];
  dp[0][0] = 0;
  dp[0][1] = 0;
  int ans = arr[1];
  dp[1][0] = dp[1][1] = arr[1];
  FOR(i,2,n+1){
    dp[i][0] = max(dp[i-1][0] + arr[i],arr[i]);
    dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0]);
    ans = max(ans,max(dp[i][0],dp[i][1]));
  }

  cout << ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}