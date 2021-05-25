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
const int MX = 4000010;

ll n;
int numbers[MX];



void solve(){
    cin >> n;

    FOR(i,2,n+1) numbers[i] = i;

    FOR(i,2,n+1){
        if(numbers[i] == 0) continue;
        for(int j = i + i; j <= n; j += i){
            numbers[j] = 0;
        }
    }
    vector<int> candidate;
    FOR(i,2,n+1){
        if(numbers[i]) candidate.push_back(i);

    }

    vector<ll> pref(candidate.size() + 1);
    REP(i,candidate.size()){
        // what_is(candidate[i]);
        pref[i + 1] = pref[i] + candidate[i];
    }

    int s = 0;
    int e = 1;

    int ans = 0;

    while(s < pref.size()-1){
        int ret = pref[e] - pref[s];
        if(ret == n) ans++;
        if(ret < n){
            if(e == pref.size() - 1) s++;
            else e++;
        }
        if(ret >= n) s++;
    }

    cout << ans << "\n";
    
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}