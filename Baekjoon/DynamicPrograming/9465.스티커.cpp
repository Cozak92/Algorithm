#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 100000;

int dp[2][MX];
int arr[2][MX];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t,n;
    cin >> t;
    while(t--){
        cin >> n;

        REP(i,n) cin >> arr[0][i];
        REP(i,n) cin >> arr[1][i];

        dp[0][0] = arr[0][0];
        dp[1][0] = arr[1][0];
        dp[0][1] += dp[1][0] + arr[0][1];
        dp[1][1] += dp[0][0] + arr[1][1];

        FOR(i,2,n){
            
            dp[0][i] += max(dp[1][i-1],dp[1][i-2]) + arr[0][i];
            dp[1][i] += max(dp[0][i-1],dp[0][i-2]) + arr[1][i];
        }

        cout << max(dp[0][n-1],dp[1][n-1]) << endl;
        memset(dp,0,sizeof(dp));

    }

    
}