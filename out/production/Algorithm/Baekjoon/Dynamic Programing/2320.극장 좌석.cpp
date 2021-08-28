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

int dp[100];
int n,m;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    FOR(i,3,n+1) dp[i] = dp[i-1] + dp[i-2];

    cin >> m;
    int e = 0;
    int s = 0;
    int ans = 1;
    REP(i,m){
        cin >> e;
        ans *= dp[e - s -1];
        s = e;
    }
     
    ans *= dp[n-s];
    cout << ans;

}