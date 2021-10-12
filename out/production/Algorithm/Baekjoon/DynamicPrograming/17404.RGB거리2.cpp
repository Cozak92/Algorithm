#include <bits/stdc++.h>

using namespace std;
#define FOR(i, m, n) for (int i = (m); i < (n); i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(v) (v).begin(), (v).end()
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0,
1, 1, 1};

int house[1010][5];
int dp[1010][5][5];
int n;

int dfs(int index, int color, int first){
    if(index == n - 1){
        if( color == first){
            return 1000001;
        }
        else return house[index][color];
    }
    if(dp[index][color][first] != 1000001 ) return dp[index][color][first];

    REP(i,3){
        if(color != i){
            dp[index][color][first] = min(dp[index][color][first], dfs(index +1, i, first) + house[index][color]);
        }
    }
        
    return dp[index][color][first];
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    REP(i,n){
        REP(j,3){
            cin >> house[i][j];
            REP(k,3) dp[i][j][k] = 1000001;
        }
    }
    int ans = INF;
    REP(j,3) {
        ans = min(ans,dfs(0,j,j));
    }

    cout << ans;
}

