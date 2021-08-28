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
int n,t;
int arr[100];
ll dp[100][21];

ll dfs(int index,int cnt){
    
    if(cnt < 0 || cnt > 20) return 0;
    if(index == n - 2) return cnt == arr[n - 1];
    ll &result = dp[index][cnt];
    if(result != -1) return result;
    result = 0;

    result += ( dfs(index + 1, cnt + arr[index + 1]) + dfs(index + 1, cnt - arr[index + 1]) );
    
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;

    REP(i,n) cin >> arr[i];

    memset(dp,-1,sizeof(dp));
    
    cout << dfs(0,arr[0]) << "\n";


}