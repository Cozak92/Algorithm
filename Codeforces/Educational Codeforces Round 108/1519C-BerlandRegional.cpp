#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 1;

struct Student{
    int u,s;
};

int t;

void solve(){
    int n; cin >> n;

    vector<vector<int>> s(n);
    vector<int> a(n);

    REP(i,n) cin >> a[i], --a[i];
    REP(i,n) {
        int x;
        cin >> x;
        s[a[i]].push_back(x);
    }
    vector<ll> res(n+1);
    for(auto a : s){
        sort(a.rbegin(),a.rend());
        vector<ll> pref(a.size() + 1);
        REP(i,a.size()){
            pref[i + 1] = pref[i] + a[i];
        }

        FOR(k,1,a.size() + 1){
            res[k] += pref[a.size() / k * k];
        }
    }

    FOR(i,1,n+1){
        cout << res[i] << " ";
    }
    cout << "\n";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> t;

    while(t--) solve();
}