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
const int MX = 2021;

int n;
ll a[2020],dp[2020][2020];
int main() {
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        scanf("%lld",&a[i]);
    }
    for(int i=0;i<=n;i++) for(int j=0;j<=n;j++) dp[i][j]=-1ll<<60;
    dp[0][0]=0;
    for(int i=1;i<=n;i++) {
        for(int j=0;j<i;j++) {
            dp[i][j]=max(dp[i-1][j],dp[i][j]);
            if(dp[i][j]>=0&&dp[i-1][j]+a[i]>=0) dp[i][j+1]=max(dp[i][j+1],dp[i-1][j]+a[i]);
        }
    }
    for(int i=n;i>=0;i--) {
        if(dp[n][i]>=0) {
            printf("%d\n",i);
            return 0;
        }
    }
} 