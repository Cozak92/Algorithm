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
const int MX = 1;

void solve(){
    int n; cin >> n;
    vector<int> a;
    vector<int> ans(2*n);
    REP(i,n * 2){
        int c; cin >> c;
        a.push_back(c);
    }
    sort(ALL(a));
    int index = 0;
    for(int i = 0; i < 2 * n - 1; i += 2){
        ans[i] = a[index++];
    }
    for(int i = 1; i < 2 * n; i += 2){
        ans[i] = a[index++];
    }
    for(auto e : ans) cout << e << " ";
    cout << "\n";
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;  cin >> t;
    while(t--) solve();
}