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

ll n;
ll arr[300000];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    REP(i,n) cin >> arr[i];
    if( n == 1){
        cout << arr[0];
        exit(0);
    }
    ll ans = min(arr[0],arr[1]);
    ans = ans % MOD;
    FOR(i,1,n -1){
        ans *= min(arr[i-1],min(arr[i],arr[i+1]));
        ans = ans % MOD;
    }
    ans *= min(arr[n-2],arr[n-1]);
    ans = ans % MOD;
    cout << ans;
}